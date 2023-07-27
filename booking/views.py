from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from .models import Booking
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime, date, timedelta, time
from django.utils import timezone
from dateutil.parser import parse
from dateutil import parser
from django.urls import reverse


def get_week_start_end_dates(today_date):
    current_weekday = today_date.weekday()

    # Calculate the start and end dates for the current week, starting from Wednesday
    if current_weekday == 6:  # If today is Sunday, start from Tuesday of the next week
        start_of_week = today_date + timedelta(days=2)
    elif current_weekday == 0:  # If today is Monday, start from Tuesday
        start_of_week = today_date + timedelta(days=1)
    else:  # For all other days (Tuesday to Saturday), start from tomorrow
        start_of_week = today_date + timedelta(days=(1 - current_weekday))

    days_until_sunday = (6 - current_weekday) % 7
    end_of_week = start_of_week + timedelta(days=days_until_sunday)

    print(start_of_week)
    print(end_of_week)
    return start_of_week, end_of_week


def get_week_start_date(today):
    current_weekday = today.weekday()
    days_to_wednesday = (2 - current_weekday) % 7
    start_of_week = today + timedelta(days=days_to_wednesday)
    return start_of_week


def get_week_end_date(today):
    current_weekday = today.weekday()
    days_to_sunday = (6 - current_weekday) % 7
    end_of_week = today + timedelta(days=days_to_sunday + 1)
    return end_of_week


def get_available_slots(request):
    today_date = timezone.localdate()
    start_of_week, end_of_week = get_week_start_end_dates(today_date)

    booked_slots = Booking.objects.filter(date__range=[start_of_week, end_of_week], user=request.user).values_list(
        'date', 'time'
    )
    available_slots = []

    time_choices = Booking._meta.get_field('time').choices

    if today_date.weekday() == 6:  # If today is Sunday, start from Tuesday of the next week
        start_of_week, end_of_week = get_week_start_end_dates(today_date + timedelta(weeks=1))

    # Loop from tomorrow (Wednesday) to Sunday of the current week or next week if today is Sunday
    for day in range(1, 7):  # Start from Wednesday (day=1) to Sunday (day=6)
        current_date = start_of_week + timedelta(days=day)
        if current_date < today_date:  # If the current date is in the past, skip it
            continue
        if current_date.weekday() == 0:  # If the current date is Monday, skip it
            continue
        time_slots = []

        for hour, label in time_choices:
            current_time = time(hour)
            current_slot = datetime.combine(current_date, current_time)
            if (current_date, hour) in booked_slots:
                slot_status = 'Booked'
            else:
                slot_status = 'Available'
            time_slots.append({'time': current_slot, 'status': slot_status})

        available_slots.append({'date': current_date, 'time_slots': time_slots})

    return available_slots


# class booking_list(generic.ListView):
#     model = Booking
#     template_name = 'booking/my_bookings.html'

#     def get_queryset(self):
#         today = timezone.localdate()
#         start_of_week = get_week_start_date(today)
#         end_of_week = get_week_end_date(today)

#         queryset = self.model.objects.filter(user=self.request.user, date__range=[start_of_week, end_of_week])
#         new_date = self.request.session.get('new_date')
#         new_time = self.request.session.get('new_time')

#         if new_date and new_time:
#             new_booking = Booking(date=new_date, time=new_time, user=self.request.user)
#         self.request.session.pop('new_date', None)
#         self.request.session.pop('new_time', None)

#         return queryset
class booking_list(generic.ListView):
    model = Booking
    template_name = 'booking/my_bookings.html'

    def get_queryset(self):
        user = self.request.user
        return Booking.objects.filter(user=user).order_by('date', 'time')

        queryset = self.model.objects.filter(user=self.request.user, date__range=[start_of_week, end_of_week])

        # Get new_date and new_time from the session
        new_date = self.request.session.get('new_date')
        new_time = self.request.session.get('new_time')

        # If new_date and new_time exist, check if a new booking has been made and add it to the queryset
        if new_date and new_time:
            new_booking = Booking(date=new_date, time=new_time, user=self.request.user)
            queryset |= Booking.objects.filter(date=new_date, time=new_time, user=self.request.user)

        # Remove new_date and new_time from the session
        self.request.session.pop('new_date', None)
        self.request.session.pop('new_time', None)

        return queryset





@login_required
def booking_confirmation(request):
    date = request.GET.get('date')
    time_slot = request.GET.get('time')

    if not date or not time_slot:
        # Handle the case where date or time_slot is not available
        # Redirect or display an error message
        error_message = "No date or time slot"
        return render(request, "booking/booking_form.html", {'error_message': error_message})

    date_obj = parse(date).date()
    time_obj = parse(time_slot).time()
    time_int = int(time_obj.strftime('%I'))

    booking, created = Booking.objects.get_or_create(date=date_obj, time=time_int, user=request.user)

    if not created:
        is_available = False
    else:
        is_available = True

    if request.method == 'POST':
        if 'cancel' in request.POST:
            # Cancel the booking
            booking.delete()
            form = BookingForm()
            available_slots = get_available_slots()
            return render(request, "booking/booking_form.html", {'form': form, 'available_slots': available_slots})

        elif 'confirm' in request.POST:
            # Update booking status
            booking.is_confirmed = True
            booking.save()
            return redirect("my_bookings")

    context = {
        'booking': booking,
        'is_available': is_available
    }

    return render(request, 'booking/booking_confirmation.html', context)


@login_required
def booking_form(request):
    user = request.user
    today = datetime.today().date()
    start_of_week, end_of_week = get_week_start_end_dates(today)

    user_booking_count = Booking.objects.filter(user=user, date__range=[start_of_week, end_of_week]).count()

    if user_booking_count >= 2:
        messages.warning(request, 'You have already booked two sessions this week. You cannot book another session.')
        return redirect("my_bookings")

    form = BookingForm()
    available_slots = get_available_slots()

    return render(request, "booking/booking_form.html", {'form': form, 'available_slots': available_slots})



@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    form = BookingForm(instance=booking)
    available_slots = get_available_slots(request)  # Pass the request object to the function

    return render(request, 'booking/edit_booking.html', {
        'booking': booking,
        'form': form,
        'available_slots': available_slots,
    })



# @login_required
# def edit_booking_confirm(request, booking_id):
#     booking = get_object_or_404(Booking, id=booking_id)

#     date_comp = request.GET.get('date')  # Get the date from the query parameters
#     time_comp = request.GET.get('time')  # Get the time from the query parameters

#     if request.method == 'POST':
#         form = BookingForm(data=request.POST, instance=booking)
#         if form.is_valid():
#             form.save()
#             return redirect("my_bookings")
#     else:
#         initial_data = {'date': date_comp, 'time': time_comp}  # Use the provided date and time

#         form = BookingForm(instance=booking, initial=initial_data)

#     context = {
#         'form': form,
#         'booking': booking,
#         'date': date_comp,  # Pass the date to the template
#         'time': time_comp,  # Pass the time to the template
#     }

#     return render(request, 'booking/edit_booking_confirm.html', context)


# @login_required
# def edit_booking_confirm(request, booking_id):
#     booking = get_object_or_404(Booking, id=booking_id)

#     date_comp = None  # Assign a default value to date_comp
#     time_comp = None
#     if request.method == 'POST':
#         form = BookingForm(data=request.POST, instance=booking)
#         if form.is_valid():
#             form.save()
#             return redirect("my_bookings")
#     else:
#         new_time = request.GET.get('time')

#         if new_time:
#             time_obj = parser.parse(new_time)
#             time_comp = time_obj.strftime('%H')  # Format time as 'HH'
#             date_comp = time_obj.date()

#         initial_data = {'date': date_comp, 'time': int(time_comp)}

#         form = BookingForm(instance=booking, initial=initial_data)

#     context = {
#         'form': form,
#         'booking': booking,
#         'date': date_comp,
#         'time': time_comp,
#     }

#     return render(request, 'booking/edit_booking_confirm.html', context)

@login_required
def edit_booking_confirm(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    date_comp = request.GET.get('date')
    time_comp = request.GET.get('time')

    formatted_date_comp = None  # Variable for formatted display date
    formatted_time_comp = None  # Variable for formatted display time

    if date_comp:
        # Format date as 'Month DD, YYYY' (e.g., 'July 29, 2023')
        date_obj = datetime.strptime(date_comp, '%Y-%m-%d')
        formatted_date_comp = date_obj.strftime('%B %d, %Y')

    if time_comp:
        # Format time as 'HH' (e.g., '11')
        time_obj = parser.parse(time_comp)
        formatted_time_comp = int(time_obj.strftime('%H'))  # Convert to integer before formatting

    # Preserve the original format for hidden input fields
    initial_data = {'date': date_comp, 'time': formatted_time_comp}  # Use formatted time for the initial data

    if request.method == 'POST':
        form = BookingForm(data=request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect("my_bookings")
    else:
        form = BookingForm(instance=booking, initial=initial_data)

    # Format time choices in the form to 'HH' (e.g., '11')
    form.fields['time'].choices = [(str(time_obj), time_str) for time_obj, time_str in form.fields['time'].choices]

    context = {
        'form': form,
        'booking': booking,
        'date': formatted_date_comp,  # Use formatted date for display
        'time': formatted_time_comp,  # Use formatted time for display
    }

    return render(request, 'booking/edit_booking_confirm.html', context)

@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == "POST":
        booking.delete()
        messages.success(request, "Your booking has been deleted successfully.")
        return redirect("my_bookings")

    return render(request, 'booking/delete_booking.html')

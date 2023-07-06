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



def get_available_slots():
    today_date = timezone.localdate()
    end_of_week = today_date + timedelta(days=7)
    booked_slots = Booking.objects.filter(date__range=[today_date, end_of_week]).values_list('date', 'time')
    available_slots = []

    time_choices = Booking._meta.get_field('time').choices
    for day in range(1, 7):
        current_date = today_date + timedelta(days=day)
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

#     def get_queryset(self):
#         today = date.today()
#         end_of_week = today + timedelta(days=7)
#         return self.model.objects.filter(user=self.request.user, date__range=[today, end_of_week])
class booking_list(generic.ListView):
    model = Booking
    template_name = 'booking/my_bookings.html'  # Specify the template name

    def get_queryset(self):
        today = date.today()
        end_of_week = today + timedelta(days=7)
        queryset = self.model.objects.filter(user=self.request.user, date__range=[today, end_of_week])

        # Check if there are session variables for updated booking
        new_date = self.request.session.get('new_date')
        new_time = self.request.session.get('new_time')

        print("New Date:", new_date)
        print("New Time:", new_time)

        if new_date and new_time:
            # Create a new booking object with the updated date and time
            new_booking = Booking(date=new_date, time=new_time, user=self.request.user)
            queryset |= QuerySet([new_booking])  # Add the updated booking to the queryset

        # Clear the session variables after retrieving them
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
            # return redirect('booking_form')
            # return redirect("my_bookings")
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
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    user_booking_count = Booking.objects.filter(user=user, date__range=[start_of_week, end_of_week]).count()

    if user_booking_count >= 2:
        messages.warning(request, 'You have already booked two sessions this week. You cannot book another session.')
        return redirect("my_bookings")


    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            slot = form.cleaned_data['slot']
            date = slot.date()
            time = slot.time()

            if Booking.objects.filter(date=date, time=time).exists():
                error_message = "This slot is already booked. Please choose another slot."
                return render(request, "booking/booking_form.html", {'error_message': error_message})

            # Set session variables
            request.session['booking_date'] = str(date)
            request.session['booking_time'] = str(time)

            # Redirect to booking_confirmation view with query parameters
            return redirect('booking_confirmation?date={}&time={}'.format(str(date), str(time)))

    else:
        form = BookingForm()

    available_slots = get_available_slots()

    return render(request, "booking/booking_form.html", {'form': form, 'available_slots': available_slots})


# @login_required
# def edit_booking(request, booking_id):
#     booking = get_object_or_404(Booking, id=booking_id)
#     form = BookingForm(instance=booking)

#     if booking.user == request.user and request.method == 'POST':
#         form = BookingForm(data=request.POST, instance=booking)
#         if form.is_valid():
#             user = request.user
#             date = form.cleaned_data['date']

#             if Booking.objects.filter(date=date).exists():
#                 error_message = "This date is already booked. Please choose another date."
#                 return render(request, "booking/booking_form.html", {'form': form, 'error_message': error_message})

#             if Booking.objects.filter(user=user, date=date).exists():
#                 error_message = "You have already booked an appointment for this date."
#                 return render(request, "booking/booking_form.html", {'form': form, 'error_message': error_message})

#             form.instance.user = user
#             form.save()
#             messages.success(request, 'Your booking has been changed successfully!')
#             return redirect("my_bookings")
#         else:
#             error_message = "An error occurred. Please try again."

#     return render(request, "booking/edit_booking.html", {'form': form})
@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(data=request.POST, instance=booking)
        if form.is_valid():
            new_date = form.cleaned_data['date']
            new_time = form.cleaned_data['time']
            date = new_date
            time = new_time
            print(date)
            print(time)
            form.save()
            return redirect('edit_booking_confirm', booking_id=booking_id)
    else:
        form = BookingForm(instance=booking)

    available_slots = get_available_slots()

    return render(request, 'booking/edit_booking.html', {
        'booking': booking,
        'form': form,
        'available_slots': available_slots,
    })


# def SessionUpdate(request,pk):
# form_class=SessionForm
# post = get_object_or_404(Sessions, pk=pk)
# form = SessionForm(request.POST)
# if request.method == "POST":
#     if form.is_valid():
#         form = SessionForm(request.POST, instance=post)
#         form.save()
#         return HttpResponseRedirect('/sessions')
@login_required
def edit_booking_confirm(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    form = BookingForm(data=request.POST, instance=booking)

    new_date = request.GET.get('date')
    new_time = request.GET.get('time')
    # until here is working
    # print(new_date)
    if request.method == 'POST':
        form = BookingForm(data=request.POST, instance=booking)
        if form.is_valid():
            print("is valid the form")

            new_date = form.cleaned_data['date']
            new_time = form.cleaned_data['time']
            date = new_date
            time = new_time
            # here is showing new date and time : none
            print(new_date)
            form.save()  # Update the existing booking with the new data++

            # Update the booking's date and time
            return redirect("my_bookings")

    else:
        # the problem is that is going here instead of the post
        print("This is the else the form is not post")
        form = BookingForm(instance=booking)

    context = {
        'form': form,
        'booking': booking,
        'new_date': new_date,
        'new_time': new_time,
    }

    return render(request, 'booking/edit_booking_confirm.html', context)






# @login_required
# def edit_booking_confirm(request, booking_id):
#     booking = get_object_or_404(Booking, id=booking_id)
#     new_date = request.GET.get('date')
#     new_time = request.GET.get('time')

#     if request.method == 'POST':
#         form = BookingForm(request.POST, instance=booking)
#         if form.is_valid():
#             # Remove the previous booking
#             booking.delete()

#             # Create a new booking with the updated data
#             new_booking = form.save(commit=False)
#             new_booking.user = request.user
#             new_booking.save()
#             return redirect("my_bookings")
#     else:
#         form = BookingForm(instance=booking)

#     context = {
#         'form': form,
#         'booking': booking,
#         'new_date': new_date,
#         'new_time': new_time
#     }

#     return render(request, 'booking/edit_booking_confirm.html', context)

@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == "POST":
        booking.delete()
        messages.success(request, "Your booking has been deleted successfully.")
        return redirect("my_bookings")

    return render(request, 'booking/delete_booking.html')

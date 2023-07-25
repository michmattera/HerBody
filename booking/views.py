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

    # Calculate the start and end dates for the current week, excluding Monday
    if current_weekday == 0:  # If today is Monday, skip to Tuesday
        start_of_week = today_date + timedelta(days=1)
    else:
        days_until_tuesday = (1 - current_weekday) % 7
        start_of_week = today_date + timedelta(days=days_until_tuesday)

    end_of_week = start_of_week + timedelta(days=6)

    return start_of_week, end_of_week

def get_week_start_date(today):
    current_weekday = today.weekday()
    days_to_tuesday = (current_weekday - 1) % 7
    start_of_week = today - timedelta(days=days_to_tuesday)
    return start_of_week

def get_week_end_date(today):
    current_weekday = today.weekday()
    days_to_sunday = (6 - current_weekday) % 7
    end_of_week = today + timedelta(days=days_to_sunday)
    return end_of_week


def get_available_slots():
    today_date = timezone.localdate()
    start_of_week, end_of_week = get_week_start_end_dates(today_date)

    booked_slots = Booking.objects.filter(date__range=[start_of_week, end_of_week]).values_list('date', 'time')
    available_slots = []

    time_choices = Booking._meta.get_field('time').choices
    for day in range(0, 7):  # Adjusted range to include Sunday
        current_date = start_of_week + timedelta(days=day)
        if current_date < today_date or current_date.weekday() == 0:  # Check if the date is in the past or Monday
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


class booking_list(generic.ListView):
    model = Booking
    template_name = 'booking/my_bookings.html'

    def get_queryset(self):
        today = timezone.localdate()
        start_of_week = get_week_start_date(today)
        end_of_week = get_week_end_date(today)

        queryset = self.model.objects.filter(user=self.request.user, date__range=[start_of_week, end_of_week])
        new_date = self.request.session.get('new_date')
        new_time = self.request.session.get('new_time')

        if new_date and new_time:
            new_booking = Booking(date=new_date, time=new_time, user=self.request.user)
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
    available_slots = get_available_slots()

    return render(request, 'booking/edit_booking.html', {
        'booking': booking,
        'form': form,
        'available_slots': available_slots,
    })


@login_required
def edit_booking_confirm(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    date_comp = request.GET.get('date')  # Get the date from the query parameters
    time_comp = request.GET.get('time')  # Get the time from the query parameters

    if request.method == 'POST':
        form = BookingForm(data=request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect("my_bookings")
    else:
        initial_data = {'date': date_comp, 'time': time_comp}  # Use the provided date and time

        form = BookingForm(instance=booking, initial=initial_data)

    context = {
        'form': form,
        'booking': booking,
        'date': date_comp,  # Pass the date to the template
        'time': time_comp,  # Pass the time to the template
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

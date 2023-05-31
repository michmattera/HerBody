from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse

from . import views
from . import models
from .models import Booking
from .forms import BookingForm
from django.views.generic import DeleteView, CreateView, UpdateView, ListView
import datetime
from datetime import datetime, date, timedelta, time

from django.contrib.auth.decorators import login_required
from django.core.exceptions import NON_FIELD_ERRORS
from django.shortcuts import get_object_or_404
from django.contrib import messages

#https://stackoverflow.com/questions/24725617/how-to-make-generic-listview-only-show-users-listing

# leave = Event.objects.filter(start_date__date=today)
# today = date.today()
from django.utils import timezone

def get_available_slots():
    today_date = timezone.localdate()
    end_of_week = today_date + timedelta(days=7)
    booked_slots = Booking.objects.filter(date__range=[today_date, end_of_week]).values_list('date', 'time')
    available_slots = []

    time_choices = Booking._meta.get_field('time').choices
    for hour, label in time_choices:
        for day in range(7):
            current_date = today_date + timedelta(days=day)
            current_slot = datetime.combine(current_date, time(hour))
            if (current_date, hour) in booked_slots:
                slot_status = 'Booked'
            else:
                slot_status = 'Available'
            available_slots.append((current_slot, slot_status))

    return available_slots



class booking_list(generic.ListView):
    model = Booking

    def get_queryset(self):
        today = date.today()
        end_of_week = today + timedelta(days=7)
        return self.model.objects.filter(user=self.request.user, date__range=[today, end_of_week])



@login_required
def booking_confirmation(request, slot):
    date_time_obj = datetime.strptime(slot, '%Y-%m-%d %H:%M:%S')
    date = date_time_obj.date()
    time = date_time_obj.time().hour  # Get only the hour component of the time

    booking, created = Booking.objects.get_or_create(date=date, time=time, user=request.user)

    if not created:
        is_available = False
    else:
        is_available = True

    if request.method == 'POST':
        if 'cancel' in request.POST:
            # Cancel the booking
            booking.delete()
            return redirect('booking_cancelled')
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


# @login_required
# def booking_confirmation(request, date_time):
#     date_time_obj = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
#     time = date_time_obj.time().hour

#     try:
#         booking = Booking.objects.get(date=date_time_obj.date(), time=time)
#     except Booking.DoesNotExist:
#         # Handle the case where the booking doesn't exist
#         return HttpResponse('Booking not found.')

#     if request.method == 'POST':
#         # Process the booking confirmation or cancellation
#         if 'cancel' in request.POST:
#             # Delete the booking
#             booking.delete()
#             return redirect('booking_cancelled')
#         elif 'confirm' in request.POST:
#             # Perform any necessary actions for the confirmed booking
#             return redirect('booking_success')

#     return render(request, 'booking/booking_confirmation.html', {'booking': booking})

# @login_required
# def booking_form(request):
#     if request.POST:
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             user = request.user
#             date = form.cleaned_data['date']
            
#             # Check if any user has already booked on the selected date
#             if Booking.objects.filter(date=date).exists():
#                 error_message = "This date is already booked. Please choose another date."
#                 return render(request, "booking/booking_form.html", {'form': form, 'error_message': error_message})
            
#             # Check if the current user has already booked on the selected date
#             if Booking.objects.filter(user=user, date=date).exists():
#                 error_message = "You have already booked an appointment for this date."
#                 return render(request, "booking/booking_form.html", {'form': form, 'error_message': error_message})
            
#             form.instance.user = user
#             form.save()
#             return redirect('my_bookings')
#     else:
#         form = BookingForm()
#         available_slots = get_available_slots()
    
#     return render(request, "booking/booking_form.html", {'form': form, 'available_slots': available_slots})

@login_required
def booking_form(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            user = request.user
            slot = form.cleaned_data['slot']
            date = slot.date()
            time = slot.time()

            # Check if any user has already booked on the selected date and time
            if Booking.objects.filter(date=date, time=time).exists():
                error_message = "This slot is already booked. Please choose another slot."
                return render(request, "booking/booking_form.html", {'form': form, 'error_message': error_message})

            form.instance.user = user
            form.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
        available_slots = get_available_slots()  # Call the function to get available slots

    return render(request, "booking/booking_form.html", {'form': form, 'available_slots': available_slots})




@login_required
def edit_booking(request, booking_id):
    # model = booking
    booking = get_object_or_404(Booking, id=booking_id)
    form = BookingForm(instance=booking)
    if booking.user == request.user:
        if request.method == 'POST':
            form = BookingForm(data=request.POST, instance=booking)
        if form.is_valid():
            user = request.user
            date = form.cleaned_data['date']
                
            # Check if any user has already booked on the selected date
            if Booking.objects.filter(date=date).exists():
                error_message = "This date is already booked. Please choose another date."
                return render(request, "booking/booking_form.html", {'form': form, 'error_message': error_message})
                
            # Check if the current user has already booked on the selected date
            if Booking.objects.filter(user=user, date=date).exists():
                error_message = "You have already booked an appointment for this date."
                return render(request, "booking/booking_form.html", {'form': form, 'error_message': error_message})
                
            form.instance.user = user
            form.save()
            # messages.info(request, 'Your booking has been changed successfully!')
            messages.success(request, 'Your booking has been changed successfully!')
            return redirect("my_bookings")
        else:
            error_message = "An error occurred please try again"
        
        return render(request, "booking/edit_booking.html", {'form': form})


@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == "POST":
        booking.delete()
        messages.success(request, "Your booking has been deleted successfully")
        return redirect("my_bookings")
        
    else:
        error_message = "An error occurred please try again"
    return render(request, 'booking/delete_booking.html')
    
        
    

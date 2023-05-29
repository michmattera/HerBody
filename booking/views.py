from django.shortcuts import render, redirect
from django.views import generic
# from django.http import HttpResponse, HttpResponseRedirect
from . import views
from . import models
from .models import Booking
from .forms import BookingForm
from django.views.generic import DeleteView, CreateView, UpdateView, ListView
import datetime
from datetime import datetime, date
from django.contrib.auth.decorators import login_required
from django.core.exceptions import NON_FIELD_ERRORS
from django.shortcuts import get_object_or_404
from django.contrib import messages

#https://stackoverflow.com/questions/24725617/how-to-make-generic-listview-only-show-users-listing

# leave = Event.objects.filter(start_date__date=today)
# today = date.today()

class booking_list(generic.ListView):
    model = Booking

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


@login_required
def booking_form(request):
    if request.POST:
        form = BookingForm(request.POST)
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
            return redirect('my_bookings')
    else:
        form = BookingForm()
    
    return render(request, "booking/booking_form.html", {'form': form})


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

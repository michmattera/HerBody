from django.shortcuts import render, redirect
from django.views import generic
# from django.http import HttpResponse, HttpResponseRedirect
from . import views
from . import models
from .models import Booking
from .forms import BookingForm
from django.views.generic import DeleteView, CreateView, UpdateView, ListView
import datetime
from django.contrib.auth.decorators import login_required
from django.core.exceptions import NON_FIELD_ERRORS

#https://stackoverflow.com/questions/24725617/how-to-make-generic-listview-only-show-users-listing


class booking_list(generic.ListView):

    model = Booking

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


# @login_required
# def booking_form(request):
#     if request.POST:
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             form.instance.user = request.user
#             form.save()
#             # return render(request, "booking/booking_list.html")
#             return redirect('list')
#     else:
#         form = BookingForm()
#         return render(request, "booking/booking_form.html", {'form': form})
#     return redirect('list')
# @login_required
# def booking_form(request):
#     if request.POST:
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             user = request.user
#             date = form.cleaned_data['date']
            
#             # Check if the user already has a booking on the selected date
#             if Booking.objects.filter(user=user, date=date).exists():
#                 error_message = "You have already booked an appointment for this date."
#                 return render(request, "booking/booking_form.html", {'form': form, 'error_message': error_message})
            
#             form.instance.user = user
#             form.save()
#             return redirect('list')
#     else:
#         form = BookingForm()
    
#     return render(request, "booking/booking_form.html", {'form': form})
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
            return redirect('list')
    else:
        form = BookingForm()
    
    return render(request, "booking/booking_form.html", {'form': form})


    


def booking_delete(request):
    return


from django.shortcuts import render
from . import views
from . import models
from .models import Booking
from .forms import BookingForm
from django.views.generic import DeleteView, CreateView, UpdateView, ListView
import datetime
from django.contrib.auth.decorators import login_required



def booking_list(request):
    return render(request, "booking/booking_list.html")


# trying to create for loop for 6 days of the week
# https://pynative.com/python-create-list-of-dates-within-range/
# def days_per_week():
#     num_of_dates = 6
#     start = datetime.datetime.today()
#     date_list = [start.date() + datetime.timedelta(days=x) for x in range(num_of_dates)]
#     print('Next 6 days starting from today')
#     print(date_list)


# def booking_form(request):
#     form = BookingForm()
#     event = Booking.objects.create(
#     )
#     event.save()
#     return render(request, "booking/booking_form.html", {'form': form})

@login_required
def booking_form(request):
    if request.POST:
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "booking/booking_list.html")
    else:
        form = BookingForm()
        return render(request, "booking/booking_form.html", {'form': form})
    return render(request, "booking/booking_list.html")
    


def booking_delete(request):
    return


from django.shortcuts import render
from . import views
from . import models
from .models import Booking
from .forms import BookingForm
from django.views.generic import DeleteView, CreateView, UpdateView, ListView


def booking_list(request):
    return render(request, "booking/booking_list.html")


def booking_form(request):
    form = BookingForm()
    return render(request, "booking/booking_form.html", {'form': form})


def booking_delete(request):
    return


from django.shortcuts import render
from . import views
from . import models
from .models import Booking
from .forms import BookingForm
from django.views.generic import DeleteView, CreateView, UpdateView, ListView


# Create your views here.
class CreateBookingView(CreateView):
    """
    View to render and create bookings
    """
    form_class = BookingForm
    template_name = 'booking/booking.html'
    success_url = "/booking/managebookings/"
    model = Booking

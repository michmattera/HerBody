from django.shortcuts import render
from django.views import generic
from .models import Booking


class BookingListView(generic.ListView):
    model = Booking
    queryset = Booking.objects
    template_name = 'index.html'

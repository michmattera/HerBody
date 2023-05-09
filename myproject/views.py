from django.shortcuts import redirect, render
from django.views import generic
from django.contrib import messages
from django.views.generic import ListView, FormView

# from .forms import LoginForm
from .models import Booking


# class BookingListView(generic.ListView):
#     model = Booking
#     queryset = Booking.objects
#     template_name = 'index.html'


class Home(generic.TemplateView):
    """
    Opens to landing page
    """
    template_name = "index.html"


class About(generic.TemplateView):
    """
    Opens About page
    """
    template_name = "about.html"






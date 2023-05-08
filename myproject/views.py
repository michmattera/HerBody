from django.shortcuts import redirect, render
from django.views import generic
from django.contrib import messages
from django.contrib.auth import forms
from django.views.generic import ListView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from .models import Booking


class BookingListView(generic.ListView):
    model = Booking
    queryset = Booking.objects
    template_name = 'index.html'


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("home")
    template_name = "signup.html"


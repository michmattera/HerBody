from . import views
from django.urls import path
from . import forms
from .forms import BookingForm


urlpatterns = [
    # url for bookings
    path('booking/', forms.BookingForm, name='booking')
]
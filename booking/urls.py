from . import views
from django.urls import path, include
from . import forms
# from .forms import BookingForm


urlpatterns = [
    # url for bookings
    path('form/', views.booking_form, name='booking_form'),
    path('list/', views.booking_list, name='booking_list')

]
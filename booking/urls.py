from . import views
from django.urls import path, include
from . import forms
from .views import booking_list
# from .forms import BookingForm


urlpatterns = [
    # url for bookings
    path('form/', views.booking_form, name='booking_form'),
    # path('list/', views.booking_list, name='booking_list')
    path('list/', booking_list.as_view(), name='list'),

]
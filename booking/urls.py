from . import views
from django.urls import path, include
from . import forms
from .views import booking_list, edit_booking, delete_booking, booking_confirmation, booking_form

# from .forms import BookingForm

# app_name = 'booking'

urlpatterns = [
    # url for bookings
    path('my_bookings/', booking_list.as_view(), name='my_bookings'),
    # path('edit_booking/<booking_id>/', edit_booking, name='edit_booking'),
    # path('edit_booking/<booking_id>/', edit_booking, name='edit_booking'),
    path('edit_booking/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('booking/edit_booking_confirm/<int:booking_id>/', views.edit_booking_confirm, name='edit_booking_confirm'),
    # path('booking/edit_booking/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('delete_booking/<booking_id>/', delete_booking, name='delete_booking'),
    path('booking/book_a_session/', views.booking_form, name='booking_form'),
    path('booking/booking_confirmation/', views.booking_confirmation, name='booking_confirmation'),


]

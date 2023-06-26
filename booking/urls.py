from django.urls import path
from . import views
from .views import BookingList, edit_booking, delete_booking, booking_form, booking_confirmation

app_name = 'booking'

urlpatterns = [
    path('my_bookings/', BookingList.as_view(), name='my_bookings'),
    path('edit_booking/<int:booking_id>/', edit_booking, name='edit_booking'),
    path('delete_booking/<int:booking_id>/', delete_booking, name='delete_booking'),
    path('booking/book_a_session/', views.booking_form, name='booking_form'),
    path('booking/booking_confirmation/', booking_confirmation, name='booking_confirmation'),
]

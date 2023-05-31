from . import views
from django.urls import path, include
from . import forms
from .views import booking_list, edit_booking, delete_booking, booking_confirmation
# from .forms import BookingForm


urlpatterns = [
    # url for bookings
    # path('', include('myproject.urls'), name='myproject_urls'),
    # path('book_a_session/', views.get_available_slots, name='booking_home'),
    # path('book_a_session/', views.booking_form, name='booking_form'),
    # path('list/', views.booking_list, name='booking_list')
    path('my_bookings/', booking_list.as_view(), name='my_bookings'),
    path('edit_booking/<booking_id>/', edit_booking, name='edit_booking'),
    path('delete_booking/<booking_id>/', delete_booking, name='delete_booking'),
    path('booking/book_a_session/', views.booking_form, name='booking_form'),
    # path('booking/booking/confirmation/<str:date_time>/', views.booking_confirmation, name='booking_confirmation'),
    # path('booking/booking/booking/booking/confirmation/<slug:date_time>/', views.booking_confirmation, name='booking_confirmation')
    path('booking/confirmation/<str:slot>/', views.booking_confirmation, name='booking_confirmation'),
    






]
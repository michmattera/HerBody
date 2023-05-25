from . import views
from django.urls import path, include
from . import forms
from .views import booking_list, edit_booking
# from .forms import BookingForm


urlpatterns = [
    # url for bookings
    # path('', include('myproject.urls'), name='myproject_urls'),
    path('form/', views.booking_form, name='booking_form'),
    # path('list/', views.booking_list, name='booking_list')
    path('your_bookings/', booking_list.as_view(), name='confirmation'),
    path('edit_booking/<booking_id>/', edit_booking, name='edit_booking'),

]
from . import views
from django.urls import path
from .views import SignUpView


urlpatterns = [
    path('', views.BookingListView.as_view(), name='booking'),
    path("signup/", SignUpView.as_view(), name="signup"),
    
]

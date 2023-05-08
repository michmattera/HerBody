from . import views
from django.urls import path
from . import forms
from .forms import register
from .forms import login


urlpatterns = [
    path('', views.BookingListView.as_view(), name='booking'),
    path('register/', forms.register, name="register"),
    path("login/", forms.login, name="login"),
    
]

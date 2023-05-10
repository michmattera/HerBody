from . import views
from django.urls import path
from . import forms
from .forms import register, login, custom_logout


urlpatterns = [
    # path('', views.BookingListView.as_view(), name='booking'),
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),

    # url for account links
    path('register/', forms.register, name="register"),
    path("login/", forms.login, name="login"),
    path("logout/", forms.custom_logout, name="logout"),
]

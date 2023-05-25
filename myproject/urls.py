from . import views
from .views import About, Profile
from django.urls import path
from . import forms
from .forms import register, login, custom_logout


urlpatterns = [
    # url for navigation links
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),

    # url for account links
    path('register/', forms.register, name="register"),
    path("login/", forms.login, name="login"),
    path("logout/", forms.custom_logout, name="logout"),
    path("profile/", views.Profile.as_view(), name="profile"),
]

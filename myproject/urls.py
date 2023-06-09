from . import views
from .views import About, contact_view, register, login, custom_logout, Home

from django.urls import path

# from . import forms
# from .forms import register, login, custom_logout


urlpatterns = [
    # url for navigation links
    # path('', views.Home.as_view(), name='home'),
    path('', views.Home, name='home'),
    path('about/', views.About, name='about'),

    # url for account links
    path('register/', views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.custom_logout, name="logout"),

    # for contact links
    path("contact/", views.contact_view, name="contact"),  
]

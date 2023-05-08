from . import views
from django.urls import path
from .views import register


urlpatterns = [
    path('', views.BookingListView.as_view(), name='booking'),
    path('register/', views.register, name="register"),
    # path("signup/", SignUpView.as_view(), name="signup"),
    # path("login/", LoginView.as_view(), name="login"),
    
]

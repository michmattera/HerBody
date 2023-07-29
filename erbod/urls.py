from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

# Url importing url from other application
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myproject.urls'), name='myproject_urls'),
    path('booking/', include('booking.urls'), name='booking_urls'),
]

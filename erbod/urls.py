from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myproject.urls'), name='myproject_urls'),
    path('', TemplateView.as_view(template_name="index.html"), name="home"),
    path('booking/', include('booking.urls'), name='booking_urls'),
]

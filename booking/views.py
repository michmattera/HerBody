from django.shortcuts import render
from django.views import generic
from . import views
from . import models
from .models import Booking
from .forms import BookingForm
from django.views.generic import DeleteView, CreateView, UpdateView, ListView
import datetime
from django.contrib.auth.decorators import login_required

#https://stackoverflow.com/questions/24725617/how-to-make-generic-listview-only-show-users-listing


class booking_list(generic.ListView):

    model = Booking

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


@login_required
def booking_form(request):
    if request.POST:
        form = BookingForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return render(request, "booking/booking_list.html")
    else:
        form = BookingForm()
        return render(request, "booking/booking_form.html", {'form': form})
    return render(request, "booking/booking_list.html")
    

def booking_delete(request):
    return


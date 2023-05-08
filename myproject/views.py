from django.shortcuts import redirect, render
from django.views import generic
from django.contrib import messages
from django.contrib.auth import forms
from django.contrib.auth.models import User, auth
from django.views.generic import ListView, FormView
from django.urls import reverse_lazy
from .models import Booking


class BookingListView(generic.ListView):
    model = Booking
    queryset = Booking.objects
    template_name = 'index.html'


# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy("home")
#     template_name = "signup.html"
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password,
                                        email=email)
                user.save()
                
                return redirect('home')

        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect(register)
            
    else:
        return render(request, 'register.html')

# class LoginView(generic.)

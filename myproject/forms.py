from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import forms
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, authenticate

# https://www.javatpoint.com/django-usercreationform
# https://www.pythontutorial.net/django-tutorial/django-login/

# function to register users
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
        return render(request, 'account/register.html')


# function to login the user
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.info(request, 'You have logged in correctly')
            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login')

    else:
        # here you should select the page that you want to redirect the user
        return render(request, 'account/login.html')

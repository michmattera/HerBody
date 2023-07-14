from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.views import generic
from django.contrib import messages
from django.views.generic import ListView, FormView, TemplateView
from django import forms
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import ContactForm


# class Home(generic.TemplateView):
#     """
#     Opens to landing page
#     """
#     template_name = "index.html"
def Home(request):
    """
    Home Page
    """
    return render(request, "index.html")


def About(request):
    """
    Home Page
    """
    return render(request, "about.html")




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
        if not request.POST.get('remember_me', None):
            request.session.set_expiry(0)
        if user is not None:
            auth.login(request, user)
            messages.info(request, 'You have logged in correctly')

            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login')

    else:
        return render(request, 'account/login.html')


@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home")


def contact_view(request):
    """
    Contact Page and Form
    """
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = "Website Inquiry"

            body = {
			'name': form.cleaned_data['name'], 
			'subject': form.cleaned_data['subject'], 
			'email': form.cleaned_data['email'], 
			'message':form.cleaned_data['message'], 
			}

            message = "\n".join(body.values())

            messages.success(request, 'You have submitted the form correctly!')
            form.save()
            return redirect('/')
        else:
            messages.error(
                request,
                "Failed to send message. Please try again. All fields are required.",
            )
            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("/")

    if request.user.is_authenticated:
        form = ContactForm(initial={'email': request.user.email, 'name' : request.user.username})
    else:
        form = ContactForm()

    context = {"form": form}
    return render(request, "contact/contact.html", context)


def map(request):
    key = settings.GOOGLE_MAP_API_KEY
    context = {
        'key': key,
    }
    return render(request, 'google/map.html',context)
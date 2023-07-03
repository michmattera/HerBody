from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.views import generic
from django.contrib import messages
from django.views.generic import ListView, FormView, TemplateView
from .forms import ContactForm
from django import forms
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


class Home(generic.TemplateView):
    """
    Opens to landing page
    """
    template_name = "index.html"


class About(generic.TemplateView):
    """
    Opens About page
    """
    template_name = "about.html"


class Profile(generic.TemplateView):
    """
    Opens Profile page
    """
    template_name = "account/profile.html"


# def get_user_profile(request, username):
#     user = User.objects.get(username=username)
#     return render(request, 'myproject/user_profile.html', {"user":user})
# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # Process the form data
#             form.save()
#             return redirect('/')
#     else:
#         form = ContactForm()
#     return render(request, 'contact/contact.html', {'form': form})
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
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.views import generic
from django.contrib import messages
from django.views.generic import ListView, FormView, TemplateView
from .forms import ContactForm
from django import forms


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
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            pass
            return redirect('/')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})

# def success(request):
#    return HttpResponse('Success!')



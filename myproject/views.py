from django.shortcuts import redirect, render
from django.views import generic
from django.contrib import messages
from django.views.generic import ListView, FormView


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






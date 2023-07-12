from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Contact

# https://www.javatpoint.com/django-usercreationform
# https://www.pythontutorial.net/django-tutorial/django-login/


class ContactForm(forms.ModelForm):
    """
    Contact Form
    """
    # email = forms.EmailField(required=True)
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'contact-field form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'contact-field form-control'}))
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Subject', 'class': 'contact-field form-control'}))
    message = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Write your message here!', 'class': 'message-field form-control'}))

    class Meta:
        model = Contact
        fields = (
            "name",
            "email",
            "subject",
            "message",
        )

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        message = cleaned_data.get("message")
        return cleaned_data


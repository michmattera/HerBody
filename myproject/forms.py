from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# https://www.javatpoint.com/django-usercreationform


class signUpForm(UserCreationForm):
    class meta:
        model = User
        fields = ['Username', 'Email', 'Password1', 'Password2']

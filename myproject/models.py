from django.db import models
from datetime import datetime, date
from . import forms
from django.contrib.auth.models import User


# class LoginForm(models.Model):
#     username = models.CharField()
#     password = models.CharField(widget=models.password)
#     remember_me = models.BoolenField()
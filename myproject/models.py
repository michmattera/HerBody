from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User


# class LoginForm(models.Model):
#     username = models.CharField()
#     password = models.CharField(widget=models.password)
#     remember_me = models.BoolenField()
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.email
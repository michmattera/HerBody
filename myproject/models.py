from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User


class Contact(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE,
    #                          null=True
    #                          )
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)
    
    def __str__(self):
        return f"{self.name}, {self.email}"

    class Meta:
        # Name for admin panel
        verbose_name = "Contact Form Submission"
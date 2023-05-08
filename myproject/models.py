from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User


class Booking(models.Model):
    """
    Model for booking private lesson
    Model will save User, date, time of the lesson chosen
    """
    TIME_CHOISES = (
        ("9:00 - 10:00 AM", "9:00 - 10:00 AM"),
        ("11:00 - 12:00 AM", "11:00 - 12:00 AM"),
        ("16:30 PM - 17:30 PM", "16:30 PM - 17:30 PM"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(default=datetime.now)
    time = models.CharField(choices=TIME_CHOISES, max_length=32, blank=False)

    def __str__(self):
        return f"Private session for {self.user} on {self.date} at {self.time}"


# class client(models.Model):
#     """
#     model to save user after sign up
#     saving username, password and email
#     """
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     username = models.CharField(max_length=50, help_text="username")
#     email = models.EmailField(
#         max_length=50, blank=True, unique=True, help_text="Enter email"
#     )
#     password = models.CharField(max_length=50)

#     class Meta:
#         """
#         Controls default ordering of records when querying the Model type.
#         """

#         ordering = ["username"]





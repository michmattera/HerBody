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

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="booking_name")
    date = models.DateField(default=datetime.now)
    time = models.IntegerField(choices=TIME_CHOISES, max_length=32, blank=False)

    class Meta:
        ordering = ['date', 'time']

    def __str__(self):
        return f"Private session for {self.user} on {self.date} at {self.time}"

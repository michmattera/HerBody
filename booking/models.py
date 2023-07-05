from django.db import models
from datetime import datetime, date
import datetime
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

TIME_CHOISES = (
        (9, "9:00 - 10:00 AM"),
        (11, "11:00 - 12:00 AM"),
        (16, "16:30 PM - 17:30 PM"),
    )


class Booking(models.Model):
    """
    Model for booking private lesson
    Model will save User, date, time of the lesson chosen
    """
    def Date_validation(value):
        if value < datetime.date.today():
            raise ValidationError("The date cannot be in the past")
    date = models.DateField(default=datetime.date.today, validators=[Date_validation])
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="hiuser", default=User)
    time = models.IntegerField(choices=TIME_CHOISES, blank=False, default=9)

    class Meta:
        ordering = ['date', 'time']
        unique_together = ("date", "time")

    def __str__(self):
        return f"Private session for {self.user} on {self.date} at {self.time}"


from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User

STATUS = ((0, "Available"), (1, "Unavailable"))


# DAYS_OF_WEEK = (
#     (0, 'Tuesday'),
#     (1, 'Wednesday'),
#     (2, 'Thursday'),
#     (3, 'Friday'),
#     (4, 'Saturday'),
#     (5, 'Sunday'),
# )

TIME_CHOISES = (
        (9, "9:00 - 10:00 AM"),
        (11, "11:00 - 12:00 AM"),
        (16, "16:30 PM - 17:30 PM"),
    )


# class WeekDay(models.Model):
#     user = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name="weekday"
#     )
#     weekday = models.IntegerField(choices=DAYS_OF_WEEK)


# class AvailableHour(models.Model): #Based on weekday
#     weekday = models.ForeignKey(
#         WeekDay,
#         on_delete=models.CASCADE,
#         related_name="available_hour"
#     )
#     date = models.DateField(default=datetime.now)
#     time = models.IntegerField(choices=TIME_CHOISES, blank=False, default=9)


class Booking(models.Model):
    """
    Model for booking private lesson
    Model will save User, date, time of the lesson chosen
    """

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="booking_name")
    date = models.DateField(default=datetime.now)
    # days_of_week = models.IntegerField(choices=DAYS_OF_WEEK, default=0)
    time = models.IntegerField(choices=TIME_CHOISES, blank=False, default=9)
    # status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['date', 'time']

    def __str__(self):
        return f"Private session for {self.user} on {self.date} at {self.time}"

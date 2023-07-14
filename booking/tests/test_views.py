from booking.views import get_available_slots
from datetime import timedelta
from django.test import TestCase, Client
from django.utils import timezone
from django.contrib.auth.models import User

from booking.models import Booking


class GetAvailableSlotsTests(TestCase):
    def test_get_available_slots(self):
        # Create a user
        user = User.objects.create_user(username='testuser', password='testpassword')
        
        today_date = timezone.localdate()
        end_of_week = today_date + timedelta(days=7)
        Booking.objects.create(date=today_date, user=user, time=9)

        available_slots = get_available_slots()

        self.assertEqual(len(available_slots), 6)  # There should be slots for 6 days (excluding today)
        for slot in available_slots:
            self.assertEqual(len(slot['time_slots']), 3)  # Each day should have 3 time slots
            if slot['date'] == today_date:
                self.assertEqual(slot['time_slots'][0]['status'], 'Booked')  # The booked slot should be marked as 'Booked'
            else:
                self.assertEqual(slot['time_slots'][0]['status'], 'Available')  # Other slots should be marked as 'Available'
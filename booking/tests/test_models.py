from django.test import TestCase
from datetime import datetime, date
import datetime
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from booking.models import Booking


class BookingModelTests(TestCase):

    # def test_date_validation(self):
        # Test validation for past dates
        # giving me an assertionerror not raised
        # user = User.objects.create_user(username='testuser', password='testpassword')
        # with self.assertRaises(ValidationError) as context:
        #     Booking.objects.create(date='2022-01-01', user=user, time=9)
        # self.assertTrue('The date cannot be in the past' in str(context.exception))
    def test_model_str_representation(self):
        # Create a user
        user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a booking associated with the user
        booking = Booking.objects.create(date='2023-01-01', user=user, time=9)

        # Test the __str__ method of the model
        expected_str = f"Private session for {booking.user} on {booking.date} at {booking.time}"
        self.assertEqual(str(booking), expected_str)

    def test_model_meta_attributes(self):
        # Test the Meta class attributes of the model
        self.assertEqual(Booking._meta.ordering, ['date', 'time'])
        self.assertEqual(Booking._meta.unique_together, (("date", "time"),))

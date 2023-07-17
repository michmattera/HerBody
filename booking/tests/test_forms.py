from django.test import TestCase
from booking.forms import BookingForm
from booking.models import Booking
from datetime import datetime, timedelta
from django.contrib.auth.models import User


class BookingFormTest(TestCase):
    # Setting up the user and the booking
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword')
        self.booking = Booking.objects.create(
            user=self.user,
            date=datetime.now().date(),
            time=9)

    # Test if the booking form with the wrong data is not valid
    def test_booking_form_invalid_date(self):
        # Test invalid data for the form (date in the future)
        data = {
            'date': datetime.now().date() + timedelta(days=11),
            'time': 1}
        form = BookingForm(data=data)
        self.assertFalse(form.is_valid())

    # Test if the booking form with the right data is valid
    def test_booking_form_valid(self):
        form_data = {
            'date': datetime.now().date() + timedelta(days=1),
            'time': 9,
        }
        form = BookingForm(data=form_data)
        print(form.errors)
        self.assertTrue(form.is_valid())

    # Test if with wrong time the form is not valid
    def test_booking_form_invalid_time(self):
        # Test with an invalid time (e.g., outside available slots)
        form_data = {
            'date': datetime.now().date() + timedelta(days=1),
            'time': 20,
        }
        form = BookingForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('time', form.errors)
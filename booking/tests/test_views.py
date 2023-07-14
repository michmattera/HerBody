from datetime import date, timedelta, datetime
from django.test import TestCase, Client
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from booking.views import get_available_slots
from booking.views import booking_list
from booking.views import booking_form
from booking.views import booking_confirmation

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


class BookingListViewTests(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create bookings for the user
        today = date.today()
        end_of_week = today + timedelta(days=7)
        for day in range(7):
            Booking.objects.create(date=today + timedelta(days=day), time=9, user=self.user)

        # Set up the client
        self.client = Client()
        self.client.force_login(self.user)

    def test_booking_list_view(self):
        # Call the booking_list view
        url = reverse('my_bookings')
        response = self.client.get(url)

        # Assert the expected outcome
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 7)  # Ensure all bookings are retrieved



class BookingFormViewTests(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Set up the client
        self.client = Client()
        self.client.force_login(self.user)

    # def test_booking_form_view(self):
    #     # Create bookings for the user
    #     today = datetime.today().date()
    #     start_of_week = today - timedelta(days=today.weekday())
    #     end_of_week = start_of_week + timedelta(days=6)
    #     Booking.objects.create(date=start_of_week, time=9, user=self.user)

    #     # Call the booking_form view with a POST request
    #     url = reverse('booking_form')
    #     response = self.client.post(url, {'slot': datetime.now().isoformat()})

    #     # Print response content for debugging
    #     print(response.content)

    #     # Assert the expected outcome
    #     self.assertRedirects(response, reverse('booking_confirmation') + '?date={}&time={}'.format(today.isoformat(), '09:00:00'))


    def test_booking_form_view_exceed_limit(self):
        # Create two bookings for the user within the week
        today = datetime.today().date()
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        Booking.objects.create(date=start_of_week, time=9, user=self.user)
        Booking.objects.create(date=start_of_week, time=11, user=self.user)

        # Call the booking_form view with a GET request
        url = reverse('booking_form')
        response = self.client.get(url)

        # Print response content for debugging
        print(response.content)

        # Assert the expected outcome
        self.assertRedirects(response, reverse('my_bookings'))


class BookingConfirmationViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_booking_confirmation_view(self):
        # Log in the user
        self.client.force_login(self.user)

        # Make a GET request to the booking_confirmation view
        url = reverse('booking_confirmation')
        response = self.client.get(url)

        # Assert the response status code
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is used
        self.assertTemplateUsed(response, 'booking/booking_form.html')

        # Assert that the user is passed to the template context
        self.assertEqual(response.context['user'], self.user)

        # You can add more assertions to verify the behavior of the view

    def test_booking_confirmation_requires_authentication(self):
        # Create a test user
        username = 'testuser123'  # Unique username
        password = 'testpassword'
        user = User.objects.create_user(username=username, password=password)

        # Log out the user to simulate a non-authenticated request
        self.client.logout()

        # Make a GET request to the booking_confirmation view
        url = reverse('booking_confirmation')
        response = self.client.get(url)

        # Assert that the response redirects to the login page
        self.assertRedirects(response, reverse('login') + '?next=' + url)


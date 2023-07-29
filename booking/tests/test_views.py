# importing what is needed for unittest
from datetime import date, timedelta, datetime
from django.test import TestCase, Client
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import RequestFactory
# importing from the views
from booking.views import get_available_slots
from booking.views import booking_list
from booking.views import booking_form
from booking.views import booking_confirmation
from booking.views import get_week_start_end_dates
from booking.views import get_week_start_date
from booking.views import get_week_end_date
# importing from forms and models
from booking.models import Booking
from booking.forms import BookingForm


# Testing getting start and end of the week correctly
class TestGetWeekStartEndDates(TestCase):

    def test_sunday(self):
        # Today is Sunday (weekday 6)
        today_date = date(2023, 7, 30)
        start_of_week, end_of_week = get_week_start_end_dates(today_date)
        self.assertEqual(start_of_week, date(2023, 8, 1))
        self.assertEqual(end_of_week, date(2023, 8, 6))

    def test_monday(self):
        # Today is Monday (weekday 0)
        today_date = date(2023, 7, 31)
        start_of_week, end_of_week = get_week_start_end_dates(today_date)
        self.assertEqual(start_of_week, date(2023, 8, 1))
        self.assertEqual(end_of_week, date(2023, 8, 7))  # Corrected value

    def test_tuesday_to_saturday(self):
        # Today is Tuesday (weekday 1)
        today_date = date(2023, 8, 1)
        start_of_week, end_of_week = get_week_start_end_dates(today_date)
        self.assertEqual(start_of_week, date(2023, 8, 1))
        self.assertEqual(end_of_week, date(2023, 8, 6))

        # Today is Saturday (weekday 5)
        today_date = date(2023, 8, 5)
        start_of_week, end_of_week = get_week_start_end_dates(today_date)
        self.assertEqual(start_of_week, date(2023, 8, 1))
        self.assertEqual(end_of_week, date(2023, 8, 6))


# Testing get available slot
class GetAvailableSlotsTests(TestCase):

    def setUp(self):
        # Create a test user and log in as that user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_get_available_slots(self):
        # Create bookings for testing (You can adjust the dates and times as needed)
        Booking.objects.create(date=date(2023, 7, 29), time=9, user=self.user)
        Booking.objects.create(date=date(2023, 7, 30), time=11, user=self.user)

        # Call the get_available_slots function
        today_date = timezone.localdate()
        available_slots = get_available_slots(today_date)

        # Assert that the available_slots variable is not empty
        self.assertIsNotNone(available_slots)

        # Assert the structure of available_slots
        self.assertIsInstance(available_slots, list)

        for slot in available_slots:
            self.assertIsInstance(slot, dict)
            self.assertIn('date', slot)
            self.assertIn('time_slots', slot)
            self.assertIsInstance(slot['date'], date)  # Changed to date
            self.assertIsInstance(slot['time_slots'], list)

            for time_slot in slot['time_slots']:
                self.assertIsInstance(time_slot, dict)
                self.assertIn('time', time_slot)
                self.assertIn('status', time_slot)
                self.assertIsInstance(time_slot['time'], datetime)
                self.assertIn(time_slot['status'], ['Available', 'Booked'])


# Testing booking list view
class BookingListViewTests(TestCase):
    # Setting up the class with user and booking
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Create bookings for the user
        today = date.today()
        end_of_week = today + timedelta(days=7)
        for day in range(7):
            Booking.objects.create(date=today + timedelta(days=day), time=9, user=self.user)
        # Set up the client and force login
        self.client = Client()
        self.client.force_login(self.user)

    def test_booking_list_view(self):
        # Call the booking_list view
        url = reverse('my_bookings')
        response = self.client.get(url)
        # Assert the expected outcome
        self.assertEqual(response.status_code, 200)
        # Ensure all bookings are retrieved
        self.assertEqual(len(response.context['object_list']), 7)


# Test booking form view
class BookingFormViewTest(TestCase):
    # Setting up the class with user
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword')

    def test_booking_form_get(self):
        # Log in the user
        self.client.force_login(self.user)
        # Send GET request to the booking_form view
        response = self.client.get(reverse('booking_form'))
        # Assert that the response is successful
        self.assertEqual(response.status_code, 200)
        # Assert that the form and available slots are present in the response
        self.assertIsInstance(response.context['form'], BookingForm)
        self.assertIsNotNone(response.context['available_slots'])

    def test_booking_form_user_limit_exceeded(self):
        # Log in the user
        self.client.force_login(self.user)
        # Create a booking with a unique date and time
        today = datetime.today().date()
        start_of_week = today - timedelta(days=today.weekday())
        Booking.objects.create(
            user=self.user,
            date=start_of_week + timedelta(days=7), time=9)
        # Send GET request to the booking_form view
        response = self.client.get(reverse('booking_form'))
        # Assert that the response is successful
        self.assertEqual(response.status_code, 200)
        # Assert that the form and available slots are present in the response
        self.assertIsInstance(response.context['form'], BookingForm)
        self.assertIsNotNone(response.context['available_slots'])


# Test booking confirmation view
class BookingConfirmationViewTest(TestCase):
    # Setting up the class with user
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword')

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


# Test edit booking view
class EditBookingViewTest(TestCase):
    # Setting up the class with user and booking
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword')
        self.booking = Booking.objects.create(
            user=self.user,
            date=datetime.now().date(),
            time=9)

    def test_edit_booking(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('edit_booking', args=[self.booking.id]))
        # Assert the response
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], BookingForm)
        self.assertEqual(response.context['booking'], self.booking)
        self.assertIsNotNone(response.context['available_slots'])


# Test edit booking confirm view
class EditBookingConfirmViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword')
        self.booking = Booking.objects.create(
            user=self.user,
            date=datetime.now().date(),
            time=9)

    def test_edit_booking_confirm_get(self):
        self.client.force_login(self.user)
        new_time = '10:00'  # Provide a specific time for testing
        new_date = '2023-07-30'  # Provide a specific date for testing
        response = self.client.get(reverse(
            'edit_booking_confirm',
            args=[self.booking.id]),
            {'date': new_date, 'time': new_time})
        # Assert the response
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], BookingForm)
        self.assertIsNotNone(response.context['date'])
        self.assertIsNotNone(response.context['time'])

    def test_edit_booking_confirm_post(self):
        self.client.force_login(self.user)
        new_date = datetime.now().date() + timedelta(days=1)
        new_time = None  # Set new_time to None
        form_data = {
            'date': new_date,
        }
        response = self.client.post(reverse(
            'edit_booking_confirm',
            args=[self.booking.id]), data=form_data)
        self.assertEqual(response.status_code, 200)
        # Check if the booking has not been updated
        updated_booking = Booking.objects.get(id=self.booking.id)
        # Assert the response
        self.assertEqual(updated_booking.date, self.booking.date)
        self.assertEqual(updated_booking.time, self.booking.time)


# Testing delete booking view
class DeleteBookingViewTest(TestCase):
    # Setting up the class with user and booking
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword')
        self.booking = Booking.objects.create(user=self.user, date=datetime.now().date(), time=9)

    # Force login, and test the reverse status
    def test_delete_booking(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse(
            'delete_booking',
            args=[self.booking.id]))
        self.assertEqual(response.status_code, 200)

    # Force login, test redirect , and check if the booking has been deleted
    def test_delete_booking_post(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse(
            'delete_booking',
            args=[self.booking.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('my_bookings'))
        # Check if the booking has been deleted
        with self.assertRaises(Booking.DoesNotExist):
            Booking.objects.get(id=self.booking.id)

# importing what is needed for unittest
from datetime import date, timedelta, datetime
from django.test import TestCase, Client
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# importing from the views
from booking.views import get_available_slots
from booking.views import booking_list
from booking.views import booking_form
from booking.views import booking_confirmation
# importing from froms and models
from booking.models import Booking
from booking.forms import BookingForm


# Testing available slots function
class GetAvailableSlotsTests(TestCase):

    def test_get_available_slots(self):
        user = User.objects.create_user(
            username='testuser',
            password='testpassword')
        today_date = timezone.localdate()
        end_of_week = today_date + timedelta(days=7)
        Booking.objects.create(date=today_date, user=user, time=9)
        available_slots = get_available_slots()
        self.assertEqual(len(available_slots), 6) 
        # There should be slots for 6 days (excluding today)
        for slot in available_slots:
            # Each day should have 3 time slots
            self.assertEqual(len(slot['time_slots']), 3)
            if slot['date'] == today_date:
                # The booked slot should be marked as 'Booked'
                self.assertEqual(slot['time_slots'][0]['status'], 'Booked')  
            else:
                 # Other slots should be marked as 'Available'
                self.assertEqual(slot['time_slots'][0]['status'], 'Available')  


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
    # Setting up the class with user and booking
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword')
        self.booking = Booking.objects.create(
            user=self.user,
            date=datetime.now().date(), time=9)

    def test_edit_booking_confirm_get(self):
        self.client.force_login(self.user)
        new_time = '10:00'  # Provide a specific time for testing
        response = self.client.get(reverse(
            'edit_booking_confirm',
            args=[self.booking.id]),
            {'time': new_time})
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






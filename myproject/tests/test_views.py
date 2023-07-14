from django.test import TestCase, Client
from django.urls import resolve
from django.urls import reverse
from myproject.views import Home, About, register, login, custom_logout
from django.contrib.auth import get_user_model
from django.test import RequestFactory
from django.contrib import auth, messages
from django.shortcuts import redirect, render


class TestTemplates(TestCase):
    """
    Testing templates render
    """

    def setUp(self):
        # set up user
        self.client = Client()

    def test_home_url_renders(self):
        # Test home page renders correctly
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_url_template_is_correct(self):
        # Test home page template is correct
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "index.html")

    def test_about_url(self):
        # Test about page renders correctly
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "about.html")

    def test_contact_url(self):
        # Test contact page renders correctly
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact/contact.html")


class RegisterTests(TestCase):
    # Create SetUp with all fields for register model
    def setUp(self):
        self.username = 'testuser'
        self.email = 'testuser@email.com'
        self.password = 'secret1'
        self.confirm_password = 'secret1'
        
    def test_register_page_url(self):
        # Test register url
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

    def test_register_page_view_name(self):
        # Test register template
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='account/register.html')

    def test_register_form(self):
        # Test register form
        response = self.client.post(reverse('register'), data={
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'confirm_password': self.confirm_password
        })
        self.assertEqual(response.status_code, 302)
        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)


class LoginViewTests(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = auth.get_user_model().objects.create_user(username=self.username, password=self.password)

    def test_login_valid_credentials(self):
        # Prepare test data
        data = {
            'username': self.username,
            'password': self.password,
        }

        # Call the view function
        response = self.client.post(reverse('login'), data=data)

        # Assert the expected outcome
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')
        self.assertEqual(messages.get_messages(response.wsgi_request).__iter__().__next__().message, 'You have logged in correctly')

    def test_login_invalid_credentials(self):
        # Prepare test data
        data = {
            'username': 'invaliduser',
            'password': 'invalidpassword',
        }

        # Call the view function
        response = self.client.post(reverse('login'), data=data)

        # Assert the expected outcome
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/login/')
        self.assertEqual(messages.get_messages(response.wsgi_request).__iter__().__next__().message, 'Invalid Username or Password')

    def test_login_get_request(self):
        # Call the view function
        response = self.client.get(reverse('login'))

        # Assert the expected outcome
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')


class LogoutViewTests(TestCase):
    def setUp(self):
        self.user = auth.get_user_model().objects.create_user(username='testuser', password='testpassword')

    def test_logout_view(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Call the view function
        response = self.client.get(reverse('logout'))

        # Assert the expected outcome
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')
        self.assertEqual(messages.get_messages(response.wsgi_request).__iter__().__next__().message, 'Logged out successfully!')

        # Check if the user is logged out
        self.assertFalse(auth.get_user(self.client).is_authenticated)



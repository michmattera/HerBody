from django.test import TestCase, Client
from django.urls import resolve
from django.urls import reverse
from .views import Home, About, register
from . import views
from django.contrib.auth import get_user_model


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
        self.register_url = reverse('register')
        
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

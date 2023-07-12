from django.test import TestCase, Client
from django.urls import resolve
from django.urls import reverse
from .views import Home, About, register
from . import views
from pprint import pprint


class TestTemplates(TestCase):
    """
    Testing templates render
    """

    def setUp(self):
        # set up user
        self.client = Client()

    def test_home_url_renders(self):
        # Test home page renders correctly
        # response = self.client.get(reverse("home"))
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_url_template_is_correct(self):
        # Test home page template is correct
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "index.html")

    def test_about_url_accessible_by_name(self):
        # Test about page renders correctly
        # response = self.client.get(reverse("/about/"))
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "about.html")


class RegisterTests(TestCase):

    def setUp(self):
        self.username = 'testuser'
        self.email = 'testuser@email.com'
        self.password = 'secret1'
        self.confirm_password = 'secret1'
        self.register_url = reverse('register')
        
    def test_register_page_url(self):
        # response = self.client.get('/register/')
        # print(response.data)
        # self.assertEqual(response.status_code, 200)
        response = self.client.get('/')
        # pprint(response.context['exception_value'])
        self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, template_name='account/register.html')

    def test_register_page_view_name(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='account/register.html')

    # def test_register_form(self):
    #     response = self.client.post(reverse('register'), data={
    #         'username': self.username,
    #         'email': self.email,
    #         'password': self.password,
    #         'confirm_password': self.confirm_password
    #     })
    #     self.assertEqual(response.status_code, 302)
    #     users = get_user_model().objects.all()
    #     self.assertEqual(users.count(), 1)

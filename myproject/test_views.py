from django.test import TestCase, Client

from django.urls import reverse
from .views import Home, About
from . import views


class TestTemplates(TestCase):
    """
    Testing templates render
    """

    def setUp(self):
        # set up user
        self.client = Client()

    def test_home_url_renders(self):
        # Test home page renders correctly
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_home_url_template_is_correct(self):
        # Test home page template is correct
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "index.html")

    def test_about_url_accessible_by_name(self):
        # Test about page renders correctly
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "about.html")
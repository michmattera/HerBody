from django.test import TestCase, Client
from .forms import ContactForm
# from .forms import custom_logout

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.urls import reverse
# test for the contact form and view
from .views import contact_view

# https://stackoverflow.com/questions/68680262/django-testing-how-to-make-a-request-as-logged-in-user


class TestContactForm(TestCase):

    def test_form_is_valid(self):
        # test form is valid
        form_data = {"name": "name1", "email": "test@email.com" , "subject": "testing", "message": "This is a test if the form works"}
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())
        
    def test_contact_form_name_field_label(self):
        # test field label for date
        form = ContactForm()
        self.assertTrue(
            form.fields["name"].label is None
            or form.fields["name"].label == "name1"
        )

    def test_contact_form_email_field_label(self):
        # test field label for date
        form = ContactForm()
        self.assertTrue(
            form.fields["email"].label is None
            or form.fields["email"].label == "email"
        )

    def test_contact_form_subject_field_label(self):
        # test field label for date
        form = ContactForm()
        self.assertTrue(
            form.fields["subject"].label is None
            or form.fields["subject"].label == "subject"
        )
        
    def test_contact_form_message_field_label(self):
        # test field label for date
        form = ContactForm()
        self.assertTrue(
            form.fields["message"].label is None
            or form.fields["message"].label == "message"
        )

    def test_contact_form_submission(self):
        # Test contact form posts to database
        contact = contact_view.objects.last()
        self.assertEqual(contact.name, "name")
        self.assertEqual(contact.email, "test@email.com")
        self.assertEqual(
            contact.message,
            "This is a test if the form works"
        )


# class register_test(TestCase):

#     @classmethod
#     def setUp(cls):
#         """
#         Create a user
#         """
#         client = Client()
#         id = 1
#         username = "test_username"
#         email = "test@test.com"
#         password = "secret"
#         test_user = User.objects.create_user(username, email, password)


#     def test_register_form(self):
#         form_data = {"username": "name", "email": "test@email.com" , "password": "secret", "confirm_password": "secret"}
#         form = register(data=form_data)
#         self.assertTrue(form.is_valid())
# class TestLogout(TestCase):

#     @classmethod
#     def setUp(cls):
#         """
#         Create a user
#         """
#         client = Client()
#         id = 1
#         username = "test_username"
#         email = "test@test.com"
#         password = "secret"
#         test_user = User.objects.create_user(username, email, password)

#     def test_logout(self):
#         self.client.login(username="test_username", password="secret")
#         response = self.client.get(redirect("/logout/"))
#         self.assertEqual(response.status_code, 200)
   

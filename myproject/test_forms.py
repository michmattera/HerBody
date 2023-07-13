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
from .models import Contact

# https://stackoverflow.com/questions/68680262/django-testing-how-to-make-a-request-as-logged-in-user


class TestContactForm(TestCase):

    def test_contact_form_is_valid_and_submit_correctly(self):
        # test form is valid
        form_data = {"name": "name1", "email": "test@email.com" , "subject": "testing", "message": "This is a test if the form works"}
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())
        form.save()
        # Retrieve the contact object from the database
        contact = Contact.objects.last()
        # Assert the expected outcome
        self.assertEqual(contact.name, "name1")
        self.assertEqual(contact.email, "test@email.com")
        self.assertEqual(contact.subject, "testing")
        self.assertEqual(contact.message, "This is a test if the form works")
        
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


   

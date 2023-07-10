from django.test import TestCase
from .forms import register
from .forms import ContactForm

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError


class TestContactForm(TestCase):

    def test_form_is_valid(self):
        # test form is valid
        form_data = {"name": "name", "email": "test@email.com" , "subject": "testing", "message": "passwordtesting"}
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())
        
    def test_contact_form_name_field_label(self):
        # test field label for date
        form = ContactForm()
        self.assertTrue(
            form.fields["name"].label is None
            or form.fields["name"].label == "name"
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
   

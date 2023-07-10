from django.test import TestCase, Client
from .forms import register
from .forms import ContactForm
from .forms import custom_logout

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.urls import reverse

# https://stackoverflow.com/questions/68680262/django-testing-how-to-make-a-request-as-logged-in-user


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
    
    # def test_contact_redirects(self):
    #     # Test contact form posts is shown
    #     self.assertEqual(ContactForm.objects.count(), 1)
    #     response = self.client.get(reverse("contact"))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, "contact.html")



class RegisterTests(TestCase):

    def setUp(self):
        # self.username = 'testuser'
        # self.email = 'testuser@email.com'
        # self.password = 'secret1'
        # self.confirm_password = 'secret1'
        self.register_url = reverse('register')

    def test_register_page_url(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='account/register.html')

    def test_register_page_view_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='account/register.html')

    def test_register_form(self):
        response = self.client.post(redirect('home'), data={
            'username': self.username,
            'email': self.email,
            'password1': self.password,
            'confirm_password': self.confirm_password
        })
        self.assertEqual(response.status_code, 302)

        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)
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
   

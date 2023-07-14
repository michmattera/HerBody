from django.test import TestCase
from myproject.models import Contact


class ContactModelTest(TestCase):
    """
    Test Contact Model
    """

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Contact.objects.create(
            name="Test",
            email="test@test.com",
            subject="Test",
            message="testing",
        )

    def test_name_label(self):
        # Test name label shows correctly
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_email_label(self):
        # Test email label shows correctly
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field("email").verbose_name
        self.assertEqual(field_label, "email")

    def test_date_posted_label(self):
        # Test date_posted label shows correctly
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field("subject").verbose_name
        self.assertEqual(field_label, "subject")
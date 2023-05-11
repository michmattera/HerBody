from datetime import datetime
from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    Form to create booking
    """
    class Meta:
        """ Set fields and labels """
        model = Booking
        fields = [
            'user', 'date', 'time'
            ]
        date = forms.DateField(help_text="Date must be a future date")
        labels = {
            'user': 'Name',
            'date': 'Date',
            'time': 'Time',
        }
from datetime import datetime
from django import forms
from .models import Booking

#https://stackoverflow.com/questions/73436899/initialize-django-modelform-user-field-with-current-logged-user
class BookingForm(forms.ModelForm):
    """
    Form to create booking
    """
    class Meta:
        """ Set fields and labels """
        model = Booking
        fields = [
            'date', 'time'
            ]

        
class DateInput(forms.DateInput):
    input_type = 'date'


class LastActiveForm(forms.Form):
    """
    Last Active Date Form
    """
    last_active = forms.DateField(widget=DateInput)

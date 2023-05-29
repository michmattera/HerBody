from datetime import datetime
from django import forms
from .models import Booking
# from bootstrap_datepicker_plus.widgets import DatePickerInput

#https://stackoverflow.com/questions/73436899/initialize-django-modelform-user-field-with-current-logged-user
class BookingForm(forms.ModelForm):
    """
    Form to create booking
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
                }
            )

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

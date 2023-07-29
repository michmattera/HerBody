from datetime import datetime
from django.utils import timezone
from datetime import datetime, date, timedelta, time
from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    Form to create booking
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['time'].widget = forms.HiddenInput()
        self.fields['date'].widget = forms.HiddenInput()

    class Meta:
        """ Set fields and labels """
        model = Booking
        fields = ['date', 'time']

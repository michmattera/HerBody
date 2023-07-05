from datetime import datetime
from django.utils import timezone
from datetime import datetime, date, timedelta, time

from django import forms
from .models import Booking
# from bootstrap_datepicker_plus.widgets import DatePickerInput

#https://stackoverflow.com/questions/73436899/initialize-django-modelform-user-field-with-current-logged-user
# class BookingForm(forms.ModelForm):
#     """
#     Form to create booking
#     """
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['date'].widget = forms.widgets.DateInput(
#             attrs={
#                 'type': 'date',
#                 'class': 'form-control',
#                 'min': 'datetime.date.today',
#                 'max': 'datetime.datetime.today() + datetime.timedelta(days=6)'
#                 }
#             )

#     class Meta:
#         """ Set fields and labels """
#         model = Booking
#         fields = [
#             'date', 'time'
#             ]

class BookingForm(forms.ModelForm):
    """
    Form to create booking
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
                'min': 'datetime.date.today',
                'max': 'datetime.datetime.today() + datetime.timedelta(days=6)'
            }
        )
        self.fields['time'].widget = forms.widgets.TimeInput(
            attrs={
                'type': 'time',
                'class': 'form-control'
            }
        )

    class Meta:
        """ Set fields and labels """
        model = Booking
        fields = [
            'date', 'time'
        ]


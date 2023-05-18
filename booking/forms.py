from datetime import datetime
from django import forms
from .models import Booking
# from .models import AvailableHour
# from .models import WeekDay


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
        # date = forms.DateField(help_text="Date must be a future date")
        # labels = {
        #     'date': 'Date',
        #     'time': 'Time'
        # }

# class TicketCreate(CreateView):
#     model = Ticket
#     template_name = "tickets/ticket_form.html"
#     fields = ['title', 'description']

#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         form.instance.user = Profile.objects.get(user=self.request.user)
#         return super(TicketCreate, self).form_valid(form)

        
class DateInput(forms.DateInput):
    input_type = 'date'


class LastActiveForm(forms.Form):
    """
    Last Active Date Form
    """
    last_active = forms.DateField(widget=DateInput)

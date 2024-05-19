from django import forms
from .models import Booking
from .models import Inquiry

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['consultant', 'date', 'time']

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['name', 'email', 'message']

from django import forms
from .models import Booking, Inquiry, Consultant

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['consultant', 'date', 'time']

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['name', 'email', 'message']


#  Search and Filter Forms

class SearchForm(forms.Form):
    consultant_name = forms.CharField(required=False, label='Consultant Name')

class FilterForm(forms.Form):
    date = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date'}))
    specialty = forms.ModelChoiceField(queryset=Consultant.objects.values_list('specialties', flat=True).distinct(), required=False)

# Booking Status Form

class BookingStatusForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['status']
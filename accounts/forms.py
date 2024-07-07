from django import forms
from .models import Booking, Inquiry, Consultant, Review
from django.utils import timezone
from django.core.exceptions import ValidationError


class BookingForm(forms.ModelForm):
    date = forms.DateField(input_formats=['%m-%d-%Y'])

    class Meta:
        model = Booking
        fields = ['consultant', 'date', 'time']

    def clean_date(self):
        date = self.cleaned_data['date']
        if date < timezone.now().date():
            raise ValidationError("The date cannot be in the past.")
        return date


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['name', 'email', 'message']


# Search and Filter Forms

class SearchForm(forms.Form):
    consultant_name = forms.CharField(required=False, label='Consultant Name')


class FilterForm(forms.Form):
    date = forms.DateField(
        required=False,
        widget=forms.TextInput(attrs={'type': 'date'})
    )
    specialty = forms.ModelChoiceField(
        queryset=Consultant.objects.values_list('specialties', flat=True)
        .distinct(),
        required=False
    )


# Booking Status Form

class BookingStatusForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['status']


# User Reviews and Feedback System

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comments']

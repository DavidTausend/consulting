from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Booking
from .forms import BookingForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:login'))  
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def home(request):
    return render(request, 'accounts/home.html')

@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.client = request.user
            if not Booking.objects.filter(consultant=booking.consultant, date=booking.date, time=booking.time).exists():
                booking.save()
                return redirect('accounts:booking_list')
            else:
                form.add_error(None, 'This slot is already booked.')
    else:
        form = BookingForm()
    return render(request, 'accounts/create_booking.html', {'form': form})

@login_required
def booking_list(request):
    bookings = Booking.objects.filter(client=request.user)
    return render(request, 'accounts/booking_list.html', {'bookings': bookings})
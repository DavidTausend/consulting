from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import (
    Booking, Consultant, Inquiry, Review, Portfolio, Certificate
)
from .forms import (
    BookingForm, InquiryForm, SearchForm, FilterForm,
    BookingStatusForm, ReviewForm
)
from django.contrib.admin.views.decorators import staff_member_required
from django_ratelimit.decorators import ratelimit
from django.db import connection
from django.contrib import messages


# Create your views here.


# Register to the website
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:login'))
    else:
        form = UserCreationForm()
    response = render(request, 'accounts/register.html', {'form': form})
    connection.close()
    return response


# Home page
def home(request):
    response = render(request, 'accounts/home.html')
    connection.close()
    return response


# Create booking
@login_required
def create_booking(request):
    consultants = Consultant.objects.all()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.client = request.user
            if not Booking.objects.filter(
                consultant=booking.consultant, date=booking.date, time=booking.time
            ).exists():
                booking.save()
                messages.success(request, "Booking created successfully!")
                return redirect('accounts:booking_list')
            else:
                messages.error(request, "This slot is already booked.")
    else:
        form = BookingForm()
    return render(request, 'accounts/create_booking.html', {'form': form, 'consultants': consultants})


# Booking list
@login_required
def booking_list(request):
    bookings = Booking.objects.filter(client=request.user)
    response = render(
        request,
        'accounts/booking_list.html',
        {'bookings': bookings}
    )
    connection.close()
    return response


# Consultant Profiles
def consultant_list(request):
    consultants = Consultant.objects.all()
    response = render(
        request,
        'accounts/consultant_list.html',
        {'consultants': consultants}
    )
    connection.close()
    return response


def consultant_profile(request, consultant_id):
    consultant = get_object_or_404(Consultant, id=consultant_id)
    response = render(
        request,
        'accounts/consultant_profile.html',
        {'consultant': consultant}
    )
    connection.close()
    return response


# Contact Information and Inquiry Form
def contact(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your inquiry has been submitted successfully!")
            return redirect('accounts:contact_confirmation')
    else:
        form = InquiryForm()
    return render(request, 'accounts/contact.html', {'form': form})


def contact_confirmation(request):
    response = render(request, 'accounts/contact_confirmation.html')
    connection.close()
    return response


# Search and Filter Requests
def consultation_list(request):
    bookings = Booking.objects.all()
    search_form = SearchForm(request.GET)
    filter_form = FilterForm(request.GET)

    if search_form.is_valid():
        consultant_name = search_form.cleaned_data.get('consultant_name')
        if consultant_name:
            bookings = bookings.filter(
                consultant__name__icontains=consultant_name
            )

    if filter_form.is_valid():
        date = filter_form.cleaned_data.get('date')
        specialty = filter_form.cleaned_data.get('specialty')
        if date:
            bookings = bookings.filter(date=date)
        if specialty:
            bookings = bookings.filter(
                consultant__specialties__icontains=specialty
            )

    response = render(
        request,
        'accounts/consultation_list.html',
        {
            'bookings': bookings,
            'search_form': search_form,
            'filter_form': filter_form,
        }
    )
    connection.close()
    return response


# Admin Views for Bookings Management
@staff_member_required
def admin_dashboard(request):
    bookings = Booking.objects.all()
    response = render(
        request,
        'accounts/admin_dashboard.html',
        {'bookings': bookings}
    )
    connection.close()
    return response


@staff_member_required
def update_booking_status(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingStatusForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            connection.close()
            return redirect('accounts:admin_dashboard')
    else:
        form = BookingStatusForm(instance=booking)
    response = render(
        request,
        'accounts/update_booking_status.html',
        {'form': form, 'booking': booking}
    )
    connection.close()
    return response


# Update booking
@login_required
def update_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, client=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, "Booking updated successfully!")
            return redirect('accounts:booking_list')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'accounts/update_booking.html', {'form': form})
    

# User Reviews and Feedback System
@login_required
def submit_review(request, consultant_id):
    consultant = get_object_or_404(Consultant, id=consultant_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.consultant = consultant
            review.user = request.user
            review.save()
            messages.success(request, "Review submitted successfully!")
            return redirect('accounts:view_reviews', consultant_id=consultant.id)
    else:
        form = ReviewForm()
    return render(request, 'accounts/submit_review.html', {'form': form, 'consultant': consultant})


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Review updated successfully!")
            return redirect('accounts:view_reviews', consultant_id=review.consultant.id)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'accounts/edit_review.html', {'form': form, 'review': review})


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    consultant_id = review.consultant.id
    review.delete()
    messages.success(request, "Review deleted successfully!")
    return redirect('accounts:view_reviews', consultant_id=consultant_id)


def view_reviews(request, consultant_id):
    """
    Retrieves all reviews for a specific consultant and displays them.
    """
    consultant = get_object_or_404(Consultant, id=consultant_id)
    reviews = Review.objects.filter(consultant=consultant)

    return render(request, 'accounts/view_reviews.html', {
        'consultant': consultant,
        'reviews': reviews
    })


def portfolio_list(request):
    portfolios = Portfolio.objects.all()
    response = render(
        request,
        'accounts/portfolio_list.html',
        {'portfolios': portfolios}
    )
    connection.close()
    return response


def certificate_list(request):
    certificates = Certificate.objects.all()
    response = render(
        request,
        'accounts/certificate_list.html',
        {'certificates': certificates}
    )
    connection.close()
    return response


# Deleting Reviews
@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    review.delete()
    return redirect('accounts:view_reviews', consultant_id=review.consultant.id)

# Deleting Booking
@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, client=request.user)
    booking.delete()
    messages.success(request, "Booking deleted successfully!")
    return redirect('accounts:booking_list')


def about_me(request):
    about_me_content = {
        "bio": (
            "I'm a passionate Cloud Engineer and Programmer with a deep "
            "affection for felines and a knack for mending computers. I "
            "find immense joy in crafting intricate lines of code and "
            "architecting cloud solutions that shape the digital world. "
            "When I'm not immersed in the realm of technology, you'll "
            " my beloved cats, drawing inspiration from their curiosity and "
            "often find me in the company of playfulness. My fascination with"
            " computers extends beyond the virtual, as I also thrive on the "
            "hands-on experience of diagnosing and repairing hardware. With "
            "every project and every computer I fix, I'm driven by a desire to"
            " create and innovate, both in the world of programming and in the"
            " day-to-day interactions with the technology we rely on. Welcome "
            "to my portfolio, where these passions come to life."
        )
    }
    response = render(request, 'accounts/about_me.html', about_me_content)
    connection.close()
    return response


@ratelimit(key='ip', rate='5/m', method='POST', block=True)
def my_view(request):
    pass


def my_view(request):
    connection.close()
    return render(request, 'home.html')

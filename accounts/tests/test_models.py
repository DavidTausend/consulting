from django.test import TestCase
from django.contrib.auth.models import User
from accounts.models import (
    Consultant,
    Booking,
    Inquiry,
    Review,
    Portfolio,
    Certificate,
)
from datetime import datetime, timedelta


class ConsultantModelTest(TestCase):
    def setUp(self):
        self.consultant = Consultant.objects.create(
            name="John Doe",
            title="Senior Consultant",
            bio="Expert in cloud computing",
            specialties="AWS, GCP, DevOps",
        )

    def test_consultant_creation(self):
        self.assertEqual(self.consultant.name, "John Doe")
        self.assertEqual(str(self.consultant), "John Doe")


class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.consultant = Consultant.objects.create(
            name="Jane Doe", title="Data Scientist", bio="ML Specialist", specialties="AI, ML, Data Science"
        )
        self.booking = Booking.objects.create(
            user=self.user,
            consultant=self.consultant,
            date=datetime.now().date(),
            time="14:00",
            status="Pending",
        )

    def test_booking_creation(self):
        self.assertEqual(self.booking.user.username, "testuser")
        self.assertEqual(str(self.booking), f"{self.user.username} - {self.consultant.name} ({self.booking.date})")


class InquiryModelTest(TestCase):
    def setUp(self):
        self.inquiry = Inquiry.objects.create(
            name="Alice Johnson",
            email="alice@example.com",
            message="Looking for a DevOps consultant",
        )

    def test_inquiry_creation(self):
        self.assertEqual(self.inquiry.name, "Alice Johnson")
        self.assertEqual(str(self.inquiry), "Inquiry from Alice Johnson")


class ReviewModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="reviewer", password="password123")
        self.consultant = Consultant.objects.create(
            name="Alex Smith", title="IT Specialist", bio="Experienced IT consultant", specialties="Networking, Security"
        )
        self.review = Review.objects.create(
            user=self.user,
            consultant=self.consultant,
            rating=5,
            comment="Excellent service!",
        )

    def test_review_creation(self):
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(str(self.review), f"Review by {self.user.username} for {self.consultant.name}")


class PortfolioModelTest(TestCase):
    def setUp(self):
        self.consultant = Consultant.objects.create(
            name="Michael Brown", title="AI Engineer", bio="Deep Learning Enthusiast", specialties="NLP, Vision"
        )
        self.portfolio = Portfolio.objects.create(
            consultant=self.consultant,
            title="AI Chatbot",
            description="Developed an AI-powered chatbot for customer support.",
        )

    def test_portfolio_creation(self):
        self.assertEqual(self.portfolio.title, "AI Chatbot")
        self.assertEqual(str(self.portfolio), "AI Chatbot")


class CertificateModelTest(TestCase):
    def setUp(self):
        self.consultant = Consultant.objects.create(
            name="Sarah Wilson", title="Cybersecurity Expert", bio="Expert in penetration testing", specialties="Security, Compliance"
        )
        self.certificate = Certificate.objects.create(
            consultant=self.consultant,
            title="Certified Ethical Hacker",
            issued_by="EC-Council",
            issue_date=datetime.now().date() - timedelta(days=365),
        )

    def test_certificate_creation(self):
        self.assertEqual(self.certificate.title, "Certified Ethical Hacker")
        self.assertEqual(str(self.certificate), "Certified Ethical Hacker - EC-Council")


# Run tests using:
# python manage.py test accounts
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.models import (
    Consultant, Booking, Inquiry, Review, Portfolio, Certificate
)


class AccountsViewsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="password"
        )
        self.consultant = Consultant.objects.create(
            name="John Doe",
            title="Senior Consultant",
            bio="An experienced consultant.",
            specialties="Cloud Computing"
        )
        self.client.login(username="testuser", password="password")

    def test_home_view(self):
        response = self.client.get(reverse('accounts:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/home.html')

    def test_register_view(self):
        response = self.client.get(reverse('accounts:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')

    def test_create_booking_view(self):
        response = self.client.get(reverse('accounts:create_booking'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/create_booking.html')

    def test_booking_list_view(self):
        response = self.client.get(reverse('accounts:booking_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/booking_list.html')

    def test_consultant_list_view(self):
        response = self.client.get(reverse('accounts:consultant_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/consultant_list.html')

    def test_consultant_profile_view(self):
        response = self.client.get(
            reverse('accounts:consultant_profile', args=[self.consultant.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/consultant_profile.html')

    def test_contact_view(self):
        response = self.client.get(reverse('accounts:contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/contact.html')

    def test_contact_confirmation_view(self):
        response = self.client.get(reverse('accounts:contact_confirmation'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/contact_confirmation.html')

    def test_portfolio_list_view(self):
        response = self.client.get(reverse('accounts:portfolio_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/portfolio_list.html')

    def test_certificate_list_view(self):
        response = self.client.get(reverse('accounts:certificate_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/certificate_list.html')

    def test_about_me_view(self):
        response = self.client.get(reverse('accounts:about_me'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/about_me.html')
    
    def test_booking_list_view_unauthorized(self):
        self.client.logout()
        response = self.client.get(reverse('accounts:booking_list'))
        self.assertNotEqual(response.status_code, 200)
        self.assertRedirects(response, f"{reverse('accounts:login')}?next={reverse('accounts:booking_list')}")

    def test_create_booking_invalid_input(self):
        response = self.client.post(
            reverse('accounts:create_booking'),
            {'consultant': self.consultant.id, 'date': '', 'time': ''}
        )
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'date', 'This field is required.')

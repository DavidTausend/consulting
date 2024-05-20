from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='accounts:home'), name='logout'),
    path('create_booking/', views.create_booking, name='create_booking'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('consultants/', views.consultant_list, name='consultant_list'),
    path('consultants/<int:consultant_id>/', views.consultant_profile, name='consultant_profile'),
    path('contact/', views.contact, name='contact'),
    path('contact_confirmation/', views.contact_confirmation, name='contact_confirmation'),
    path('consultations/', views.consultation_list, name='consultation_list'),
    path('', views.home, name='home'),
]

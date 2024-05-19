from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Consultant(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='consultant_pictures/', blank=True, null=True)
    specialties = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Booking(models.Model):
    consultant = models.ForeignKey(Consultant, on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"{self.consultant} - {self.client} - {self.date} {self.time}"

class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry from {self.name} - {self.email}"
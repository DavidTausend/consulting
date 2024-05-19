from django.contrib import admin
from .models import Consultant, Booking, Inquiry

# Register your models here.
admin.site.register(Consultant)
admin.site.register(Booking)
admin.site.register(Inquiry)
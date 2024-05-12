from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to login page after successful registration
            return redirect(reverse('login'))  # Ensure you have a URL named 'login'
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

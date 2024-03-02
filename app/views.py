# accounts/views.py

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from .forms import CustomUserCreationForm, SignUpForm
from .models import Doctor


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.user_type == 1:
                return redirect('patient_dashboard')
            else:
                return redirect('doctor_dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.user_type == 1:
                    return redirect('patient_dashboard')
                else:
                    return redirect('doctor_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# views.py continued

def patient_dashboard_view(request):
    # Assuming the user is logged in
    return render(request, 'patient_dashboard.html', {'user': request.user})


def doctor_dashboard_view(request):
    # Assuming the user is logged in
    return render(request, 'doctor_dashboard.html', {'user': request.user})

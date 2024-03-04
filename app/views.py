# accounts/views.py

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_protect

from .forms import CustomUserCreationForm


def login_required_view(request):
    if request.user.user_type == 1:
        return redirect('patient_dashboard')
    else:
        return redirect('doctor_dashboard')


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

def home_view(request):
    if request.user.is_authenticated:
        if request.user.user_type == 1:
            return redirect('patient_dashboard')
        elif request.user.user_type == 2:
            return redirect('doctor_dashboard')
    # Redirect to login page if user is not authenticated
    return redirect('login')


@login_required
def doctor_dashboard_view(request):
    # Assuming the user is logged in
    if request.user.user_type == 2:
        doctor_info = request.user  # Assuming the logged-in user is a doctor
        return render(request, 'doctor_dashboard.html', {'doctor_info': doctor_info})
    else:
        return redirect('patient_dashboard')


def patient_dashboard_view(request):
    # Assuming the user is logged in
    if request.user.user_type == 1:
        patient_info = request.user  # Assuming the logged-in user is a patient
        return render(request, 'patient_dashboard.html', {'patient_info': patient_info})
    else:
        return redirect('doctor_dashboard')


def signup_view_at_home(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            if request.user.user_type == 1:
                return redirect('patient_dashboard')
            elif request.user.user_type == 2:
                return redirect('doctor_dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


@csrf_protect
def my_view(request):
    # Your view logic here
    if request.user.user_type == 1:
        patient_info = request.user  # Assuming the logged-in user is a patient
        return render(request, 'patient_dashboard.html', {'patient_info': patient_info})
    elif request.user.user_type == 2:
        doctor_info = request.user  # Assuming the logged-in user is a doctor
        return render(request, 'doctor_dashboard.html', {'doctor_info': doctor_info})
    else:
        return redirect('login')

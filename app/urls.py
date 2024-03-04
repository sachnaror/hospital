
from django.urls import path

from . import views

# urls.py

urlpatterns = [
    path('', views.signup_view_at_home, name='signup'),
    path('login/', views.login_view, name='login'),
    path('dashboard/patient/', views.patient_dashboard_view,
         name='patient_dashboard'),
    path('dashboard/doctor/', views.doctor_dashboard_view, name='doctor_dashboard'),
    path('signup/', views.signup_view_at_home, name='signup'),
]

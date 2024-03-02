

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'patient'),
        (2, 'doctor'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    profile_picture = models.ImageField(upload_to='profile_pics/')
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=6)

    class Meta:
        db_table = 'app_customuser'

    def __str__(self):
        return self.username


class Doctor(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1, null=True, blank=True)

    class Meta:
        db_table = 'app_doctor'

    def __str__(self):
        return str(self.user)


class Patient(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1, null=True, blank=True)

    class Meta:
        db_table = 'app_patient'

    def __str__(self):
        return str(self.user)



from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# class User(AbstractUser):
#     groups = models.ManyToManyField(Group, related_name='custom_user_groups')
#     user_permissions = models.ManyToManyField(
#         Permission, related_name='custom_user_permissions')

#     class Meta(AbstractUser.Meta):
#         swappable = 'AUTH_USER_MODEL'
#         db_table = 'auth_user'
#         managed = True
#         verbose_name = 'user'
#         verbose_name_plural = 'users'


class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pics/')
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=6)
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(
        Permission, related_name='custom_user_permissions')


class Patient(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)


class Doctor(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from user.managers import UserManager

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=60, unique=True)
    password = models.CharField(max_length=150)
    start_date = models.DateTimeField(verbose_name='start date', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    


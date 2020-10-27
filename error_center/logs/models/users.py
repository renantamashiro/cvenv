from django.db import models

from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    username = models.CharField(('username'), max_length=15, unique=True)
    first_name = models.CharField(('first name'), max_length=30)
    last_name = models.CharField(('last name'), max_length=30)
    email = models.EmailField(('email address'), max_length=255, unique=True)

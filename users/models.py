from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(max_length=35, verbose_name='Телефон')
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Почта пользователя")
    phone = models.CharField(max_length=11, verbose_name="Номер телефона")
    avatar = models.ImageField(upload_to="users/", verbose_name="аватар", **NULLABLE)
    country = models.CharField(max_length=50, verbose_name="страна")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"




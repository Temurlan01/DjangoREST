from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import  MinLengthValidator
from django.db import models

from products.models import Pizza
from users.manager import CustomUserManager


class CustomUser(AbstractUser):
    """"Моделька для Кастомного пользователя"""
    username = None
    phone_number = models.CharField(max_length=11, validators=[MinLengthValidator(6)], unique=True)


    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        verbose_name_plural = 'Кастомные Пользователи'
        verbose_name = 'Кастомный пользователь'


class UserPizzaComment(models.Model):
    comment_text = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


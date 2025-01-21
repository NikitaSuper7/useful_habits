from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    """Модель пользователя."""

    username = models.CharField(
        max_length=30, unique=True, verbose_name="username", help_text="Укажите никнейм"
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name="email",
        help_text="Укажите адрес электронной почты",
    )
    phone_number = models.CharField(
        max_length=35,
        verbose_name="phone number",
        help_text="Укажите номер телефона",
        blank=True,
        null=True,
    )
    tg_chat_id = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="telegram id",
        help_text="Укажите ID телеграмма",
    )

    def __str__(self):
        return f"Пользователь - {self.username}, email - {self.email}"

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """
    Модель пользователя.
    """
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    country = models.CharField(max_length=20,
                               verbose_name='Страна',
                               **NULLABLE)
    avatar = models.ImageField(upload_to='users/avatars',
                               verbose_name='Аватар',
                               **NULLABLE)
    telegram_id = models.CharField(max_length=35,
                                   verbose_name='Телеграм',
                                   **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

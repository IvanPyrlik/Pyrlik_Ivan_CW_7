from datetime import timedelta

from django.conf import settings
from django.db import models

from users.models import NULLABLE


class Habits(models.Model):
    """
    Модель привычек.
    """
    PERIOD_CHOICES = [
        ('daily', 'Ежедневно'),
        ('weekly', 'Еженедельно')
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             verbose_name='Пользователь',
                             **NULLABLE)
    place = models.CharField(max_length=50,
                             verbose_name='Место выполнения')
    time = models.TimeField(verbose_name='Время выполнения')
    action = models.CharField(max_length=50,
                              verbose_name='Действие')
    is_nice_habit = models.BooleanField(default=False,
                                        verbose_name='Приятная привычка',
                                        **NULLABLE)
    related_habit = models.ForeignKey('self',
                                      on_delete=models.CASCADE,
                                      verbose_name='Связанная привычка',
                                      **NULLABLE)
    periodicity = models.CharField(max_length=50,
                                   choices=PERIOD_CHOICES,
                                   verbose_name='Периодичность',
                                   **NULLABLE)
    reward = models.CharField(max_length=50,
                              verbose_name='Вознаграждение',
                              **NULLABLE)
    duration_time = models.TimeField(default=timedelta(seconds=120),
                                     verbose_name='Время на выполнение')
    is_public = models.BooleanField(default=False,
                                    verbose_name='Признак публичности')

    def __str__(self):
        return f'{self.user} - привычка: {self.action}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'

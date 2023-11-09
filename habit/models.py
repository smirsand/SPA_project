from django.conf import settings
from django.db import models

from users.models import NULLABLE


class Habit(models.Model):
    """
    Модель привычки.
    """

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)
    place = models.CharField(max_length=150, verbose_name='Место')
    time = models.TimeField(verbose_name='Время')
    action = models.TextField(verbose_name='Действие')
    enjoyable = models.BooleanField(verbose_name='Признак приятной привычки')
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Связанная привычка', **NULLABLE)
    frequency = models.IntegerField(default=1, verbose_name='Периодичность (дни)')
    reward = models.CharField(max_length=150, verbose_name='Вознаграждение', **NULLABLE)
    time_required = models.DateTimeField(verbose_name='Время на выполнение')
    is_public = models.BooleanField(default=False, verbose_name='Признак публичности')

    def __str__(self):
        return self.action

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'

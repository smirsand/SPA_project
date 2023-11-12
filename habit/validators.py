import datetime

import pytz
from rest_framework.exceptions import ValidationError


class ExceptionValidator:
    """
    Исключает одновременный выбор полей связанная привычка и награда.
    """

    def __init__(self, related_habit, reward):
        self.related_habit = related_habit  # Связанная привычка
        self.reward = reward  # Вознаграждение

    def __call__(self, value):
        related_habit = dict(value).get(self.related_habit)
        reward = dict(value).get(self.reward)

        if related_habit and reward:
            raise ValidationError("Вы не можете выбрать одновременно связанную привычку и вознаграждение.")


class RelatedHabitsValidator:
    """
    В связанные привычки попадают только привычки с признаком приятной привычки.
    """

    def __init__(self, related_habit, enjoyable):
        self.related_habit = related_habit  # Связанная привычка
        self.enjoyable = enjoyable  # Признак приятной привычки

    def __call__(self, value):
        related_habit = dict(value).get(self.related_habit)
        enjoyable = dict(value).get(self.enjoyable)

        if related_habit and not enjoyable:
            raise ValidationError("В связанную привычку могут попадать только привычки с признаком приятной привычки.")


class NiceHabitValidator:
    """
    Приятная привычка не может быть вознаграждена или связанной привычкой.
    """

    def __init__(self, enjoyable, reward, related_habit):
        self.enjoyable = enjoyable  # Признак приятной привычки
        self.reward = reward  # Вознаграждение
        self.related_habit = related_habit  # Связанная привычка

    def __call__(self, value):
        enjoyable = dict(value).get(self.enjoyable)
        reward = dict(value).get(self.reward)
        related_habit = dict(value).get(self.related_habit)

        if enjoyable and reward is not None or related_habit is not None:
            raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки.")


class TimeValidator:
    """
    Время выполнения привычки не больше 120 секунд.
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        time = value.get(self.field)
        if time > datetime.time(minute=2):
            raise ValidationError('Время должно быть не больше 120 секунд')


class TimeHabit:
    """
    Выполнение привычки не реже, чем 1 раз в 7 дней.
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        time = value.get(self.field)
        today = datetime.datetime.today().astimezone(pytz.timezone('Europe/Moscow'))
        time_period = datetime.timedelta(days=7)
        if time - today > time_period:
            raise ValidationError('Нужно выполнять привычку не реже, чем 1 раз в 7 дней.')

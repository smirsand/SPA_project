import datetime

from rest_framework.exceptions import ValidationError


class ExceptionValidator:
    """
    Валидатор исключения одновременного выбора полей связанная привычка и награда.
    """

    def __init__(self, related_habit, reward):
        self.related_habit = related_habit
        self.reward = reward

    def __call__(self, value):
        related_habit = dict(value).get(self.related_habit)
        reward = dict(value).get(self.reward)

        if related_habit and reward:
            raise ValidationError("Вы не можете выбрать одновременно связанную привычку и награду.")


class TimeValidator:
    """
    Валидатор времени выполнения.
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        time = value.get(self.field)
        if time > datetime.time(minute=2):
            raise ValidationError('Время должно быть не больше 120 секунд')


from rest_framework import serializers

from habit.models import Habit, ReminderLog
from habit.validators import ExceptionValidator, TimeValidator, RelatedHabitsValidator, NiceHabitValidator, TimeHabit


class HabitSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели привычка.
    """

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [ExceptionValidator(related_habit='related_habit', reward='reward'),
                      RelatedHabitsValidator(related_habit='related_habit', enjoyable='enjoyable'),
                      NiceHabitValidator(enjoyable='enjoyable', reward='reward', related_habit='related_habit'),
                      TimeValidator(field='time_required'),
                      TimeHabit(field='time')]


class ReminderLogSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели журнал напоминаний.
    """

    class Meta:
        model = ReminderLog
        fields = '__all__'

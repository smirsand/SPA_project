from rest_framework import serializers

from habit.models import Habit
from habit.validators import ExceptionValidator, TimeValidator
from users.models import User


class HabitSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели привычка.
    """

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [ExceptionValidator(related_habit='related_habit', reward='reward'), TimeValidator(field='time')]


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели пользователя.
    """

    class Meta:
        model = User
        fields = '__all__'

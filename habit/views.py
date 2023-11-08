from rest_framework import generics

from habit.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """
    Контроллер создания привычки.
    """
    serializer_class = HabitSerializer

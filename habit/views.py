from rest_framework import generics

from habit.models import Habit
from habit.paginators import HabitPaginator
from habit.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """
    Контроллер создания привычки.
    """
    serializer_class = HabitSerializer


class HabitListAPIView(generics.ListAPIView):
    """
    Контроллер просмотра списка привычек.
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPaginator

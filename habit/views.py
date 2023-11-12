from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from habit.models import Habit
from habit.paginators import HabitPaginator
from habit.permissions import IsOwner
from habit.serializers import HabitSerializer
from habit.tasks import habit_telegram_bot


class HabitCreateAPIView(generics.CreateAPIView):
    """
    Контроллер создания привычки.
    """
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.owner = self.request.user
        new_habit.save()
        habit_telegram_bot.delay()  # Отложенный вызов


class HabitListAPIView(generics.ListAPIView):
    """
    Контроллер просмотра списка привычек.
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPaginator
    permission_classes = [AllowAny, IsOwner]


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """
    Контроллер просмотра привычки.
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """
    Контроллер для редактирования привычки.
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDestroyAPIView(generics.DestroyAPIView):
    """
    Контроллер для удаления привычки.
    """
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class ListPublicHabitAPIView(generics.ListAPIView):
    """
    Контроллер списка публичных привычек.
    """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_public=True)

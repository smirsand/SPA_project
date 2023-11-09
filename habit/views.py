from django.db.models import Q
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habit.models import Habit
from habit.paginators import HabitPaginator
from habit.permissions import IsOwner
from habit.serializers import HabitSerializer


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


class HabitListAPIView(generics.ListAPIView):
    """
    Контроллер просмотра списка привычек.
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Habit.objects.all()
        return Habit.objects.filter(Q(owner=self.request.user) | Q(is_public=True))


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

from django.urls import path

from habit.apps import HabitConfig
from habit.views import HabitCreateAPIView, HabitListAPIView

app_name = HabitConfig.name

urlpatterns = [
    path('habit/create/', HabitCreateAPIView.as_view(), name='habit-create'),
    path('habit/list/', HabitListAPIView.as_view(), name='habit-list'),

]

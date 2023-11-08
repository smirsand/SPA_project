from django.urls import path

from habit.apps import HabitConfig
from habit.views import HabitCreateAPIView

app_name = HabitConfig.name

urlpatterns = [
                  path('habit/create/', HabitCreateAPIView.as_view(), name='habit-create'),

              ]

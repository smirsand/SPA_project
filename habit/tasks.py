import os
from datetime import timedelta

import requests
from celery import shared_task
from django.utils import timezone

from habit.models import Habit, ReminderLog


@shared_task
def habit_telegram_bot():
    habit_list = Habit.objects.filter(is_public=True)  # Список привычек is_public=True.
    now_time = timezone.now()  # Время на данный момент.

    for habit in habit_list:
        period = habit.frequency  # Периодичность (дни). По умолчанию 1 день.
        last_reminder_log = ReminderLog.objects.filter(habit=habit).order_by('-reminder_time').first()

        if last_reminder_log:
            next_reminder_time = last_reminder_log.reminder_time + timedelta(days=period)
        else:
            next_reminder_time = habit.time + timedelta(days=period)

        if now_time >= next_reminder_time:
            text = f'Я буду {habit.action} в {habit.time} в {habit.place}'
            params = {"chat_id": os.getenv('CHAT_ID'), "text": text}
            response = requests.post(
                f"https://api.telegram.org/bot{os.getenv('TOKEN_TELEGRAM_BOT')}/sendMessage", data=params)
            if response.status_code == 200:
                print("Напоминание успешно отправлено")
            else:
                print("Ошибка при отправке напоминания")

            #  Сохраняем информацию о времени отправки сообщения
            ReminderLog.objects.create(habit=habit, reminder_time=now_time)

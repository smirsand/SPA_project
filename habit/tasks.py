from datetime import timedelta

from django.utils import timezone

from habit.models import Habit, ReminderLog
import requests
from celery import shared_task


@shared_task
def habit_telegram_bot():
    text = "Привет, как дела?"
    params = {"chat_id": 1018849724, "text": text}
    response = requests.post(
        "https://api.telegram.org/bot6849935928:AAGv29v7CTprhQFIi6CFHoM1vJvoSA_074g/sendMessage", data=params)
    if response.status_code == 200:
        print("Напоминание успешно отправлено")
    else:
        print("Ошибка при отправке напоминания")

# @shared_task
# def habit_telegram_bot():
#     habit_list = Habit.objects.filter(is_public=True)  # Список привычек.
#     # now_time = timezone.now()  # Время на данный момент.
#     #
#     for habit in habit_list:
#         # period = habit.frequency  # Периодичность (дни). По умолчанию 1 день.
#         #     last_reminder_log = ReminderLog.objects.filter(habit=habit).order_by('-reminder_time').first()
#         #
#         #     if last_reminder_log:
#         #         next_reminder_time = last_reminder_log.reminder_time + timedelta(days=period)
#         #     else:
#         #         next_reminder_time = habit.time + timedelta(days=period)
#         #
#         #     if now_time >= next_reminder_time:
#         text = f'Я буду {habit.action} в {habit.time} в {habit.place}'
#         params = {'chat_id': 1018849724, 'text': text}
#         requests.post(
#             f'https://api.telegram.org/botdjango-insecure-o8bdafg&np4&%yizrb1j2m1-!2b&1e@kr$!50@&_+@v&z=xx48/sendMessage',
#             data=params)
#         print('Напоминание отправлено')
#
#     # Сохраняем информацию о времени отправки сообщения
#     # ReminderLog.objects.create(habit=habit, reminder_time=now_time)

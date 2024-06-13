from celery import shared_task
from habits.models import Habits
from habits.services import send_message
import datetime
import pytz
from django.conf import settings


@shared_task
def send_notification():
    time_now = datetime.datetime.now(
        pytz.timezone(settings.TIME_ZONE)).time()
    habits = Habits.objects.all()

    for habit in habits:
        telegram_id = habit.user.telegram_id
        message = (
            f"Напоминание о привычке {habit.action}\n"
            f"После этого можно: "
            f"{habit.related_habit if habit.related_habit else habit.reward}"
        )
        if habit.time == time_now:
            send_message(telegram_id, message)
        habit.save()

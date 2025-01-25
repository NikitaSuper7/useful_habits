import json
from datetime import timedelta, datetime
from django.core.serializers.json import DjangoJSONEncoder
from django.utils import timezone
from config.settings import AUTH_USER_MODEL

from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from celery import shared_task

from users.models import User
from habits.models import Habits
from habits.services import send_tg_message
from habits.get_requests import current_request


@shared_task
def necessary_habits():
    """Send daily remainder."""
    today = timezone.now().date()
    tasks = Habits.objects.all()
    # print(f"Tasks - {tasks}")
    necessary_tasks = [
        json.dumps(
            {
                "id": task.pk,
                "title": task.name,
                "time_to_do": task.time_to_do,
                "owner_id": task.owner.pk,
                "owner_chat_id": task.owner.tg_chat_id,
            },
            cls=DjangoJSONEncoder,
            ensure_ascii=False,
            indent=4
        )
        for task in tasks
        if (task.last_remind.date() + timedelta(days=task.period)) < today and task.owner.tg_chat_id is not None
    ]
    print(f"Necessary Tasks - {necessary_tasks}")
    return necessary_tasks
    # send_tg_message(message=message, chat_id=user.tg_chat_id)


@shared_task
def send_tg_notification():
    """Send daily reminder."""
    current_time = timezone.now().time()
    necessary_tasks = necessary_habits()
    necessary_tasks = [json.loads(task) for task in necessary_tasks]
    # print(type(necessary_tasks[0]))
    for task in necessary_tasks:
        # print(task['time_to_do'].time())
        if (datetime.strptime(task.get('time_to_do'), "%I:%M:%S") - timedelta(
                minutes=5)).time() <= current_time and task.get('owner_chat_id'):
            message = f"У вас запланирована привычка: {task['title']}"
            send_tg_message(message=message, chat_id=task['owner_chat_id'])
            habit = Habits.objects.get(pk=task.get("id"))
            habit.last_remind = str(timezone.now())
            habit.save()
        # if task.get('owner_chat_id') is not None:
        #     message = f"У вас запланирована привычка: {task['name']}"
        #     send_tg_message(message=message, chat_id=task['owner_chat_id'])

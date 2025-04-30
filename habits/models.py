from django.db import models
from users.models import User


# Create your models here.


class Habits(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Название привычки", unique=True
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="habits",
        blank=True,
        null=True,
    )
    place = models.CharField(
        max_length=100,
        verbose_name="Место",
        help_text="Введите место, где нужно выполнить привычку, например - Дом.",
    )
    is_nice_habit = models.BooleanField(
        default=False, help_text="Это приятная привычка?"
    )
    related_habit = models.ForeignKey(
        "Habits",
        max_length=100,
        verbose_name="связанная привычка",
        help_text="Введите привычку с которой хотите связать текущую.",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    period = models.PositiveIntegerField(
        verbose_name="Частота напоминаний в днях",
        help_text="Ведите кол-ва дней через которое вам нужно будет напоминать.",
        blank=True,
        null=True,
    )
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    reward = models.TextField(
        verbose_name="Вознаграждение",
        help_text="Введите вознаграждение за выполнение привычки",
        blank=True,
        null=True,
    )
    time_length = models.PositiveIntegerField(
        verbose_name="Время на выполнение привычки",
        help_text="Введите примерное время для выполнения привычки в минутах",
        default=1,
    )
    time_to_do = models.TimeField(
        verbose_name="Время начала привычки",
        help_text="Введите время во сколько вы планируете начинать привычку",
    )
    is_public = models.BooleanField(
        default=False,
        verbose_name="Признак публичности",
        help_text="Могут ли эту привычку видеть другие пользователи?",
    )

    last_remind = models.DateTimeField(
        verbose_name="последнее напоминание", default="1900-01-01 12:00"
    )

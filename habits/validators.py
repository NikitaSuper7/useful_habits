from rest_framework.serializers import ValidationError
from habits.models import Habits


class HabitRewardValidator:
    """Проверяет, что вознаграждение только у полезной привычки."""

    def __init__(self, reward, related):
        self.reward = reward
        self.related = related

    def __call__(self, value):
        has_reward = dict(value).get(self.reward)
        has_related = dict(value).get(self.related)
        if has_reward and has_related:
            raise ValidationError(
                f"Одновременно указывать связанную привычку и вознаграждение нельзя. Выберите что-то одно"
            )


class HabitTimeValidator:
    """Проверяет, что время для выполнения привычки не превышает 120 секунд."""

    def __init__(self, time_to_do):
        self.time_to_do = time_to_do

    def __call__(self, value):
        time_in_seconds = int(dict(value).get(self.time_to_do)) * 60
        if time_in_seconds > 120:
            raise ValidationError(
                "Время для выполнения привычки не может превышать 120 секунд."
            )


class HabitRelatedValidator:
    """Проверяет, что в связанные привычки могут попадать только привычки с признаком приятной привычки."""

    def __init__(self, related):
        self.related = related

    def __call__(self, value):
        related_habit = dict(value).get(self.related)
        # related_habit = Habits.objects.get(pk=related_habit)

        if related_habit and related_habit.is_nice_habit is False:
            raise ValidationError(f"Связанная привычка должна быть приятной.")


class HabitRelatedOrRewardValidator:
    """Проверяет, что связанная привычка или вознаграждение может быть только одним из указанных."""

    def __init__(self, related, reward):
        self.related = related
        self.reward = reward

    def __call__(self, value):
        has_related = dict(value).get(self.related)
        has_reward = dict(value).get(self.reward)
        if has_related and has_reward:
            raise ValidationError(
                f"Одновременно указывать связанную привычку и вознаграждение нельзя. Выберите что-то одно"
            )


class HabitNiceValidator:
    """Проверяет, что если привычка приятная, то у нее отсутствует связанная привычка и вознагрождение."""

    def __init__(self, related, reward, is_nice):
        self.related = related
        self.reward = reward
        self.is_nice = is_nice

    def __call__(self, value):
        is_nice = dict(value).get(self.is_nice)
        has_reward = dict(value).get(self.reward)
        has_related = dict(value).get(self.related)

        if is_nice and (has_reward or has_related):
            raise ValidationError(
                f"Если привычка приятная, то у нее должно отсутствовать связанная привычка и вознаграждение."
            )


class HabitPeriodValidator:
    """Проверяет, что периодичность выполнения привычки не реже чем 1 раз в 7 дней."""

    def __init__(self, period):
        self.period = period

    def __call__(self, value):
        period = dict(value).get(self.period)
        if period > 7:
            raise ValidationError(
                "Периодичность выполнения привычки не может быть реже 1 раза в 7 дней."
            )

from rest_framework.serializers import ValidationError


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
        is_nice = dict(value).get(related_habit)

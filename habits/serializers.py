from rest_framework.serializers import ModelSerializer, SerializerMethodField

from config import settings
from habits.models import Habits
from habits.validators import (
    HabitRelatedOrRewardValidator,
    HabitTimeValidator,
    HabitRelatedValidator,
    HabitNiceValidator,
    HabitPeriodValidator,
)


# from habits.validators import VideosValidator, HasLinkValidator
# from users.services import convert_price


class HabitSerializer(ModelSerializer):
    owner = SerializerMethodField()
    validators = [
        HabitRelatedOrRewardValidator(related="related_habit", reward="reward"),
        HabitTimeValidator(time_length="time_length"),
        HabitRelatedValidator(related="related_habit"),
        HabitNiceValidator(
            related="related_habit", reward="reward", is_nice="is_nice_habit"
        ),
        HabitPeriodValidator(period="period"),
    ]

    class Meta:
        model = Habits
        fields = "__all__"

    def get_owner(self, obj):
        return obj.owner.username

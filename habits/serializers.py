from rest_framework.serializers import ModelSerializer, SerializerMethodField

from config import settings
from habits.models import Habits

# from habits.validators import VideosValidator, HasLinkValidator
# from users.services import convert_price


class HabitSerializer(ModelSerializer):
    owner = SerializerMethodField()

    class Meta:
        model = Habits
        fields = "__all__"

    def get_owner(self, obj):
        return obj.owner.username

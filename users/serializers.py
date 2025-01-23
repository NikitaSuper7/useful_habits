from rest_framework.serializers import ModelSerializer, SerializerMethodField
from users.models import User


class UserSerializer(ModelSerializer):
    """Сериалайзер пользователей."""

    class Meta:
        model = User
        fields = (
            "email",
            "username",
            "is_staff",
            "is_active",
            "is_superuser",
            "password",
        )

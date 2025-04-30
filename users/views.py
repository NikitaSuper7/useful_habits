from rest_framework.permissions import AllowAny

from users.serializers import UserSerializer

from users.models import User

# Для создания пользователя
from rest_framework.generics import CreateAPIView


# Create your views here.


class UserCreateApiView(CreateAPIView):
    """Создание нового пользователя"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        """Create a new user"""
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()

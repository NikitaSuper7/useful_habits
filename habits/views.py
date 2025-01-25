from rest_framework.permissions import IsAuthenticated, AllowAny

from habits.models import Habits
from habits.paginators import HabitPaginator
from habits.serializers import HabitSerializer
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    get_object_or_404,
)
from users.permissions import IsOwnerPermission


# Create your views here.


class HabitCreateApiView(CreateAPIView):
    """Создает привычки"""

    queryset = Habits.objects.all()
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()

    def get_permissions(self):
        self.permission_classes = (IsAuthenticated,)
        return super().get_permissions()


class HabitListApiView(ListAPIView):
    """Возвращает список привычек."""

    queryset = Habits.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = (IsOwnerPermission, IsAuthenticated)

    # def get_permissions(self):
    #     self.permission_classes = (IsOwnerPermission, IsAuthenticated)
    #     return super().get_permissions()

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)


class HabitPublicListView(ListAPIView):
    """Возвращает список публичных привычек."""

    queryset = Habits.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_public=True)


class HabitRetrieveApiView(RetrieveAPIView):
    """Возвращает одну привычку."""

    queryset = Habits.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsOwnerPermission, IsAuthenticated)


class HabitUpdateApiView(UpdateAPIView):
    """Обновляет привычку."""

    queryset = Habits.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsOwnerPermission, IsAuthenticated)


class HabitDestroyApiView(DestroyAPIView):
    """Удаляет привычку."""

    queryset = Habits.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsOwnerPermission, IsAuthenticated)

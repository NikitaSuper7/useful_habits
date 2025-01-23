from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from habits.models import Habits
from habits.serializers import HabitSerializer
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    get_object_or_404,
)
from django.shortcuts import render


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

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)


class HabitRetrieveApiView(RetrieveAPIView):
    """Возвращает одну привычку."""

    queryset = Habits.objects.all()
    serializer_class = HabitSerializer


class HabitUpdateApiView(UpdateAPIView):
    """Обновляет привычку."""

    queryset = Habits.objects.all()
    serializer_class = HabitSerializer


class HabitDestroyApiView(DestroyAPIView):
    """Удаляет привычку."""

    queryset = Habits.objects.all()
    serializer_class = HabitSerializer

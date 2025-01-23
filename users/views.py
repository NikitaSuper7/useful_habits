from django.shortcuts import render
from rest_framework import filters
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from users.serializers import UserSerializer

from users.models import User
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter, SearchFilter

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

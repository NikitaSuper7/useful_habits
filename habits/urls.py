from habits.views import (
    HabitListApiView,
    HabitCreateApiView,
    HabitUpdateApiView,
    HabitRetrieveApiView,
    HabitDestroyApiView,
)
from habits.apps import HabitsConfig
from django.urls import path

app_name = HabitsConfig.name

urlpatterns = [
    path("habits/", HabitListApiView.as_view(), name="habits_list"),
    path("habits/create/", HabitCreateApiView.as_view(), name="habits_create"),
    path(
        "habits/<int:pk>/delete/", HabitDestroyApiView.as_view(), name="habits_destroy"
    ),
    path("habits/<int:pk>/update/", HabitUpdateApiView.as_view(), name="habits_update"),
    path("habits/<int:pk>/", HabitRetrieveApiView.as_view(), name="habits_retrieve"),
]

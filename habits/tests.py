from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
from habits.models import Habits
from users.models import User


class HabitTestCase(APITestCase):
    """Тесты CRUD для привычек."""

    def setUp(self):
        self.user = User.objects.create(email="test@mail.ru", username="test")
        self.user.set_password("qwer1234")
        self.client.force_authenticate(user=self.user)
        self.habit = Habits.objects.create(
            owner=self.user,
            name="Привычка 1",
            is_nice_habit=True,
            time_to_do="12:00:00",
        )

    def test_habit_retrieve(self):
        """Проверка возврата 1-й привычки."""
        url = reverse("habits:habits_retrieve", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        # print(data)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            f"Expected {status.HTTP_200_OK}, got {response.status_code}",
        )

        self.assertEqual(data.get("name"), self.habit.name)

        self.assertEqual(data.get("is_nice_habit"), self.habit.is_nice_habit)
        self.assertEqual(
            data.get("owner"),
            self.user.username,
        )

    def test_habit_create(self):
        """Тест создания привычки."""
        url = reverse("habits:habits_create")
        data = {
            "owner": self.user,
            "name": "Привычка 2",
            "is_nice_habit": True,
            "time_to_do": "12:00:00",
            "place": "Home",
            "time_length": 1,
            "period": 2,
            # "related_habit": self.habit.pk,
        }
        response = self.client.post(url, data)
        # print(response.status_code)
        # print(response.json())
        data = response.json()
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
            f"Expected {status.HTTP_201_CREATED}, got {response.status_code}",
        )
        self.assertEqual(data.get("name"),
                         "Привычка 2")

    def test_habit_delete(self):
        """Тест на удаление привычки."""
        url = reverse("habits:habits_destroy", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
            f"Expected {status.HTTP_204_NO_CONTENT}, got {response.status_code}",
        )

        self.assertEqual(
            Habits.objects.filter(pk=self.habit.pk).exists(),
            False,
            "Habit not deleted",
        )

    def test_habit_list(self):
        """Тест списка привычек."""
        url = reverse("habits:habits_list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 2,
                    "owner": "test",
                    "name": "Привычка 1",
                    "place": "",
                    "is_nice_habit": True,
                    "period": None,
                    "date_created": "2025-01-28T08:28:40.457274+03:00",
                    "reward": None,
                    "time_length": 1,
                    "time_to_do": "12:00:00",
                    "is_public": False,
                    "last_remind": "1900-01-01T12:00:00+02:30:17",
                    "related_habit": None,
                }
            ],
        }

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            f"Expected {status.HTTP_200_OK}, got {response.status_code}",
        )
        self.assertTrue(len(data) > 0)
        self.assertEqual(data.get("name"), result.get("name"))

from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habits
from users.models import User


class HabitApiTestCase(APITestCase):
    """
    Тесты привычек.
    """

    def setUp(self):
        self.user = User.objects.create(
            email="test_user1@test.com",
            telegram_id="@test_telegram1",
            password='123'
        )
        self.habit = Habits.objects.create(
            id=11,
            user=self.user,
            place='Тест',
            time='12:00',
            action='Тест_1',
            is_nice_habit=False,
            periodicity='daily',
            duration_time='12:15',
            reward='Тест_1',
            is_public=True,
        )

    def test_create_habits(self):
        """
        Тест создания привычки.
        """
        data = {
            "user": self.user.pk,
            "place": "Тест",
            "time": "8:30",
            "action": "Тест_2",
            "reward": "Тест_2",
            "periodicity": "daily",
            "is_public": False,
            "duration_time": "09:00",
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post('/create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_habits(self):
        """
        Тест вывода списка привычек.
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/list/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_habits(self):
        """
        Тест вывода одной привычки.
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/retrieve/11/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_habits(self):
        """
        Тест удаления привычки.
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.delete('/destroy/11/')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_public_habits(self):
        """
        Тест вывода списка публичных привычек.
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/list_public/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

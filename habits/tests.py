from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from habits.models import Habits
from users.models import User


class HabitApiTestCase(APITestCase):
    """
    Тесты привычек.
    """

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email='test_user1@test.com',
            password='123'
        )
        self.client.force_authenticate(user=self.user)
        self.habit = Habits.objects.create(
            user=self.user,
            place='Тест_1',
            time='12:00',
            action='Тест_1',
            is_public=True,
            duration_time=40
        )

    def test_create_habits(self):
        """
        Тест создания привычки.
        """
        data = {
            'user': self.user.id,
            'place': 'Тест_2',
            'time': '8:30',
            'action': 'Тест_2',
            'is_public': False,
            'duration_time': 40
        }
        path = reverse('habits:create_habit')
        response = self.client.post(path, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Habits.objects.filter(action=data['action']).exists())

    def test_list_habits(self):
        """
        Тест вывода списка привычек.
        """
        response = self.client.get(reverse('habits:list_habit'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_habits(self):
        """
        Тест вывода одной привычки.
        """
        path = reverse('habits:detail_habit', [self.habit.id])
        response = self.client.get(path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['action'], self.habit.action)

    def test_update_habits(self):
        """
        Тест редактирования привычки.
        """
        path = reverse('habits:update_habit', [self.habit.id])
        data = {'place': 'test_update', 'action': 'test_update'}
        response = self.client.patch(path, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.habit.refresh_from_db()
        self.assertEqual(self.habit.action, data['action'])

    def test_delete_habits(self):
        """
        Тест удаления привычки.
        """
        path = reverse('habits:delete_habit', [self.habit.id])
        response = self.client.delete(path)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_public_habits(self):
        """
        Тест вывода списка публичных привычек.
        """
        response = self.client.get(reverse('habits:list_habit_public'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

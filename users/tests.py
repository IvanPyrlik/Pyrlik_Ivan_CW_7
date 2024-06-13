from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User


class UserAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email="test_user1@test.com",
            telegram_id="@test_telegram1",
            password='123'
        )

    def test_create_user(self):
        data = {
            "email": "test_user2@test.com",
            "telegram_id": "@test_telegram2",
            "password": "345"
        }
        response = self.client.post('/user/create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

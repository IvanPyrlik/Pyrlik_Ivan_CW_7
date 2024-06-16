from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from users.models import User


class UserAPITest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email='test_user1@test.com',
            password='123'
        )
        self.client.force_authenticate(user=self.user)

    def test_create_user(self):
        data = {
            "email": "test_user2@test.com",
            "password": "345"
        }
        path = reverse('users:register')
        response = self.client.post(path, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

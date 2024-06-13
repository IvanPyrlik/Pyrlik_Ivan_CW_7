from rest_framework import generics
from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """
    Создание пользователя.
    """
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        new_user = serializer.save()
        password = serializer.data["password"]
        new_user.set_password(password)
        new_user.save()

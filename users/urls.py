from users.views import UserCreateAPIView
from users.apps import UsersConfig
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

app_name = UsersConfig.name

urlpatterns = [
    path(
        'user/create/',
        UserCreateAPIView.as_view(),
        name='register'
    ),
    path(
        'login/',
        TokenObtainPairView.as_view(),
        name='login'
    ),
    path(
        'token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
]

from rest_framework.generics import (CreateAPIView,
                                     ListAPIView,
                                     RetrieveAPIView,
                                     UpdateAPIView,
                                     DestroyAPIView)
from rest_framework.permissions import IsAuthenticated

from habits.models import Habits
from habits.paginations import HabitsPagination
from users.permissions import IsOwner
from habits.serializers import HabitsSerializer


class HabitCreateAPIView(CreateAPIView):
    """
    Создание привычки.
    """
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitRetrieveAPIView(RetrieveAPIView):
    """
    Детальный просмотр одной привычки.
    """
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitUpdateAPIView(UpdateAPIView):
    """
    Редактор привычки.
    """
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDestroyAPIView(DestroyAPIView):
    """
    Удаление привычки.
    """
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitListAPIView(ListAPIView):
    """
    Список привычек.
    """
    serializer_class = HabitsSerializer
    pagination_class = HabitsPagination
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        user = self.request.user
        queryset = Habits.objects.filter(user=user)
        return queryset


class HabitPublicAPIView(ListAPIView):
    """
    Список публичных привычек.
    """
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all().filter(is_public=True)
    pagination_class = HabitsPagination
    permission_classes = [IsAuthenticated]

from rest_framework.serializers import ModelSerializer

from habits.models import Habits
from habits.validators import (HabitValidator,
                               TimeValidator,
                               ConnectedHabitValidator,
                               NiceHabitValidator)


class HabitsSerializer(ModelSerializer):
    """
    Сериализатор привычек.
    """

    class Meta:
        model = Habits
        fields = ["place", "time", "action", "is_nice_habit",
                  "related_habit", "periodicity",
                  "reward", "duration_time", "is_public"]
        validators = [HabitValidator(field_1='reward',
                                     field_2='related_habit'),
                      TimeValidator(field='duration_time'),
                      ConnectedHabitValidator(field_1='related_habit',
                                              field_2='is_nice_habit'),
                      NiceHabitValidator(field_1='is_nice_habit',
                                         field_2='reward',
                                         field_3='related_habit')]

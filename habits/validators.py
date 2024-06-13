from rest_framework.serializers import ValidationError


class HabitValidator:
    """
    Исключаем одновременный выбор связанной
    привычки и указания вознаграждения.
    """

    def __init__(self, field_1, field_2):
        self.field_1 = field_1
        self.field_2 = field_2

    def __call__(self, value):
        val1 = dict(value).get(self.field_1)
        val2 = dict(value).get(self.field_2)
        if val1 and val2:
            raise ValidationError(
                "Нельзя одновременно выбирать "
                "связанную привычку и вознаграждение!"
            )


class TimeValidator:
    """
    Время выполнения должно
    быть не больше 120 секунд.
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        val = dict(value).get(self.field)
        duration_seconds = (val.hour * 3600 +
                            val.minute * 60 +
                            val.second)
        if duration_seconds is not None and duration_seconds > 120:
            raise ValidationError("Время больше 120 секунд!")


class ConnectedHabitValidator:
    """
    В связанные привычки могут попадать
    только привычки с признаком приятной привычки.
    """

    def __init__(self, field_1, field_2):
        self.field_1 = field_1
        self.field_2 = field_2

    def __call__(self, value):
        related_habit = dict(value).get(self.field_1)
        is_nice_habit = dict(value).get(self.field_2)

        if related_habit is not None and not is_nice_habit:
            raise ValidationError(
                "В связанные привычки могут попадать "
                "только привычки с признаком приятной привычки"
            )


class NiceHabitValidator:
    """
    У приятной привычки не может быть
    вознаграждения или связанной привычки.
    """

    def __init__(self, field_1, field_2, field_3):
        self.field_1 = field_1
        self.field_2 = field_2
        self.field_3 = field_3

    def __call__(self, value):
        is_nice_habit = dict(value).get(self.field_1)
        reward = dict(value).get(self.field_2)
        related_habit = dict(value).get(self.field_3)
        if (is_nice_habit is True and
                (reward is not None or
                 related_habit is not None)):
            raise ValidationError(
                "У приятной привычки не может"
                "быть вознаграждения или связанной привычки!"
            )

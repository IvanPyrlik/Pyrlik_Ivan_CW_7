from django.core.management import BaseCommand
from habits.models import Habits


class Command(BaseCommand):
    """
    Добавление данных в БД.
    """

    def handle(self, *args, **options):
        Habits.objects.all().delete()

        habits_list = [
            {
                "id": 1,
                "place": "Дом",
                "time": "8:30",
                "action": "Почистить зубы",
                "periodicity": "ежедневно",
                "duration_time": 30,
                "reward": "Съесть завтрак",
                "is_public": False,
            },
            {
                "id": 2,
                "place": "Дом",
                "time": "9:00",
                "action": "Сделать зарядку",
                "periodicity": "ежедневно",
                "duration_time": 30,
                "reward": "Выпить сок",
                "is_public": False,
            },
            {
                "id": 3,
                "place": "Работа",
                "time": "12:00",
                "action": "Вымыть руки",
                "periodicity": "ежедневно",
                "duration_time": 30,
                "reward": "Съесть обед",
                "is_public": False,
            },
        ]

        habits_for_create = []
        for habit in habits_list:
            habits_for_create.append(Habits(**habit))
        Habits.objects.bulk_create(habits_for_create)

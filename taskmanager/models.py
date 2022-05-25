from django.db import models
from django.contrib.auth.models import AbstractUser


class TemporaryUser(models.Model):
    pass


class Task(models.Model):
    BLACK = 'black'
    YELLOW = 'yellow'
    BLUE = 'blue'
    GREEN = 'green'
    PINK = 'pink'

    COLORS = [
        (BLACK, 'black'),
        (YELLOW, 'yellow'),
        (BLUE, 'blue'),
        (GREEN, 'green'),
        (PINK, 'pink'),
    ]

    MONDAY = 'mo'
    TUESDAY = 'tu'
    WEDNESDAY = 'we'
    THURSDAY = 'th'
    FRIDAY = 'fr'
    SATURDAY = 'sa'
    SUNDAY = 'su'

    WEEKDAYS = [
        (MONDAY, 'mo'),
        (TUESDAY, 'tu'),
        (WEDNESDAY, 'we'),
        (THURSDAY, 'th'),
        (FRIDAY, 'fr'),
        (SATURDAY, 'sa'),
        (SUNDAY, 'su')
    ]

    temp_user = models.ForeignKey(TemporaryUser, on_delete=models.CASCADE)
    description = models.TextField(verbose_name="description", null=True, blank=True)
    deadline = models.DateField(verbose_name="deadline")
    color = models.CharField(verbose_name="color", max_length=8, choices=COLORS)
    repeating_days = models.CharField(verbose_name="repeating_days", max_length=2, null=True, blank=True, choices=WEEKDAYS)
    is_archive = models.BooleanField(verbose_name="is_archive")
    is_favorite = models.BooleanField(verbose_name="is_favorite")

    class Meta:
        verbose_name = "task"

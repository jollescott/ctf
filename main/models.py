from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

MAX_CLUE_COUNT = 10
MAX_TASK_POINTS = 100


# Create your models here.
class TaskModule(models.Model):
    """A grouping of tasks with a common theme or technique."""

    name = models.CharField(max_length=500, unique=True)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=500)
    points = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(MAX_TASK_POINTS)]
    )
    module = models.ForeignKey(TaskModule, on_delete=models.CASCADE)
    url = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name


class TaskClue(models.Model):
    clue = models.TextField()
    index = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(MAX_CLUE_COUNT)]
    )
    task = models.ForeignKey(Task, on_delete=models.CASCADE)


class TaskAttempt(models.Model):
    clue_count = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(MAX_CLUE_COUNT)]
    )
    points = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(MAX_TASK_POINTS)]
    )
    passed = models.BooleanField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

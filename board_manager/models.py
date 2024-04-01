from django.db import models
from django.utils import timezone
from users.models import User
from teams.models import Team

class Board(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=128)
    creation_time = models.DateTimeField(default=timezone.now)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)  # Foreign key to Team model


class Task(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    creation_time = models.DateTimeField(default=timezone.now)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    status_choices = [
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETE', 'Complete')
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='OPEN')



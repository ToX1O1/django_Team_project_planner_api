from django.db import models
from django.utils import timezone
from users.models import User as AuthUser

class Team(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=128)
    creation_time = models.DateTimeField(default=timezone.now)
    admin = models.ForeignKey(AuthUser, on_delete=models.CASCADE)

class TeamUser(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)

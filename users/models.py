from django.db import models
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length=64, unique=True)
    display_name = models.CharField(max_length=64)
    creation_time = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=1000)
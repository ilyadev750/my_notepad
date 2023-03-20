from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    create = models.DateTimeField(default=timezone.now())
    update = models.DateTimeField(default=timezone.now())
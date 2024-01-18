from enum import unique
from django.conf import settings
from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=255, blank=True)
    create = models.DateTimeField(default=timezone.now(), blank=True, null=True)
    update = models.DateTimeField(default=timezone.now(), blank=True, null=True)
    username_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

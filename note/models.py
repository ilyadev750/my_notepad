from enum import unique
from django.conf import settings
from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User  

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=255, null=True, blank=False)
    content = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=255, blank=False, unique=True)
    create = models.DateTimeField(default=datetime.now(), blank=True, null=True)
    update = models.DateTimeField(default=datetime.now(), blank=True, null=True)
    username_id = models.ForeignKey(User, on_delete=models.CASCADE)

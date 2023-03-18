from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



class Article(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
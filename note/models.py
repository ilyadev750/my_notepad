from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Note(models.Model):
    title = models.CharField(max_length=255, null=True, blank=False)
    content = RichTextField(blank=True, null=True)
    slug = models.SlugField(max_length=255, blank=False, unique=True)
    create = models.DateTimeField(default=None, blank=True,
                                  null=True)
    update = models.DateTimeField(default=None, blank=True,
                                  null=True)
    username_id = models.ForeignKey(User, on_delete=models.CASCADE)

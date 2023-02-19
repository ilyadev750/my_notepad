from django.db import models

from ckeditor.fields import RichTextField

class Notepad(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
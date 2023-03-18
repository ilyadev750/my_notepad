# Generated by Django 3.2.18 on 2023-03-16 13:07

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_content_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='content_upload',
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]

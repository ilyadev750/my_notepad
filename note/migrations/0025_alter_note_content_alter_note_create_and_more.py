# Generated by Django 4.2.7 on 2024-03-15 13:39

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0024_alter_note_content_alter_note_create_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='create',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='update',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]

# Generated by Django 4.2.7 on 2024-01-19 13:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0015_rename_username_note_username_id_alter_note_create_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='create',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 19, 13, 6, 26, 249946, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='update',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 19, 13, 6, 26, 250079, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]

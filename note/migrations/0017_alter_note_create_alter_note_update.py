# Generated by Django 4.2.7 on 2024-01-19 13:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0016_alter_note_create_alter_note_slug_alter_note_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='create',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 19, 13, 9, 22, 902247, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='update',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 19, 13, 9, 22, 902470, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]

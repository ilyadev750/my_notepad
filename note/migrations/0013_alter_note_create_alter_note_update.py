# Generated by Django 4.2.7 on 2024-01-18 13:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0012_alter_note_create_alter_note_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='create',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 18, 13, 34, 10, 786772, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='update',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 18, 13, 34, 10, 786927, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]

# Generated by Django 4.2.7 on 2024-03-13 01:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0040_alter_note_create_alter_note_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='create',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 13, 1, 28, 15, 40776), null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='update',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 13, 1, 28, 15, 40784), null=True),
        ),
    ]

# Generated by Django 4.2.7 on 2024-03-12 18:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0027_alter_note_create_alter_note_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='create',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 12, 18, 1, 15, 335656), null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='update',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 12, 18, 1, 15, 335664), null=True),
        ),
    ]

# Generated by Django 4.2.7 on 2024-03-12 18:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0029_alter_note_create_alter_note_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='create',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 12, 18, 22, 37, 456961), null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='update',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 12, 18, 22, 37, 456973), null=True),
        ),
    ]

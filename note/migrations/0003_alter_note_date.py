# Generated by Django 3.2.18 on 2023-03-19 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0002_alter_note_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.DateTimeField(default='18:55:28'),
        ),
    ]

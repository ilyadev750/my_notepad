# Generated by Django 3.2.18 on 2023-03-16 13:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20230316_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.2.5 on 2023-11-27 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_students_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='slug',
            field=models.SlugField(blank=True, max_length=255),
        ),
    ]

# Generated by Django 2.2 on 2020-12-22 23:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movie_show', '0002_auto_20201222_1736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movieshow',
            name='date_added',
        ),
        migrations.AddField(
            model_name='movieshow',
            name='data_added',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

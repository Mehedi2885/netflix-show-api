# Generated by Django 2.2 on 2020-12-22 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_show', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movieshow',
            name='data_added',
        ),
        migrations.AddField(
            model_name='movieshow',
            name='date_added',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

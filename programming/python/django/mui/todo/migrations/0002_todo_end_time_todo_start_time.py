# Generated by Django 4.1.3 on 2023-01-15 13:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='end_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='todo',
            name='start_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
# Generated by Django 5.0.2 on 2024-03-04 20:29

import from_db_value.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CashModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cash', from_db_value.models.CashField(decimal_places=2, max_digits=20)),
            ],
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-13 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('link', models.TextField()),
                ('time', models.CharField(max_length=100)),
                ('created_date', models.DateField()),
            ],
            options={
                'db_table': 'jobs_db',
                'ordering': ['id'],
            },
        ),
    ]

# Generated by Django 3.1.2 on 2021-02-22 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0007_personshirt'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('members', models.ManyToManyField(to='tutorial.PersonTest')),
            ],
        ),
    ]

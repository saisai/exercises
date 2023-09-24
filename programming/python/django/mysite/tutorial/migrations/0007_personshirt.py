# Generated by Django 3.1.2 on 2020-11-25 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0006_book2'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonShirt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('shirt_size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=2)),
            ],
        ),
    ]
# Generated by Django 5.0.2 on 2024-03-05 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datetimes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='approved_date',
            new_name='approval_date',
        ),
    ]

# Generated by Django 5.0.2 on 2024-03-21 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m2m_through', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='custommembership',
            options={'ordering': ['date_joined']},
        ),
        migrations.AlterField(
            model_name='group',
            name='custom_members',
            field=models.ManyToManyField(related_name='custom', through='m2m_through.CustomMembership', to='m2m_through.person'),
        ),
    ]

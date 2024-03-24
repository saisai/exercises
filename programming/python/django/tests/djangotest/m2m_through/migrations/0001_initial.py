# Generated by Django 5.0.2 on 2024-03-21 20:55

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_friended', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iname', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'ordering': ('iname',),
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rname', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'ordering': ('rname',),
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField(default=datetime.datetime.now)),
                ('invite_reason', models.CharField(max_length=64, null=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='m2m_through.group')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='m2m_through.person')),
            ],
            options={
                'ordering': ('date_joined', 'invite_reason', 'group'),
            },
        ),
        migrations.CreateModel(
            name='CustomMemberShip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField(default=datetime.datetime.now)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='m2m_through.group')),
                ('weird_fk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='m2m_through.membership')),
                ('person', models.ForeignKey(db_column='custom_person_column', on_delete=django.db.models.deletion.CASCADE, related_name='custom_person_related_name', to='m2m_through.person')),
            ],
            options={
                'db_table': 'test_table',
                'ordering': ('date_joined',),
            },
        ),
        migrations.CreateModel(
            name='PersonChild',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='m2m_through.person')),
            ],
            bases=('m2m_through.person',),
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations', to='m2m_through.event')),
                ('invitee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations', to='m2m_through.person')),
                ('inviter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations_sent', to='m2m_through.person')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='custom_members',
            field=models.ManyToManyField(related_name='custom', through='m2m_through.CustomMemberShip', to='m2m_through.person'),
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(through='m2m_through.Membership', to='m2m_through.person'),
        ),
        migrations.AddField(
            model_name='event',
            name='invitees',
            field=models.ManyToManyField(related_name='events_invited', through='m2m_through.Invitation', to='m2m_through.person'),
        ),
        migrations.CreateModel(
            name='PersonSelfRefM2M',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
                ('friends', models.ManyToManyField(through='m2m_through.Friendship', to='m2m_through.personselfrefm2m')),
            ],
        ),
        migrations.AddField(
            model_name='friendship',
            name='first',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_from_set', to='m2m_through.personselfrefm2m'),
        ),
        migrations.AddField(
            model_name='friendship',
            name='second',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_to_set', to='m2m_through.personselfrefm2m'),
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='m2m_through.ingredient', to_field='iname')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='m2m_through.recipe', to_field='rname')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(related_name='recipes', through='m2m_through.RecipeIngredient', to='m2m_through.ingredient'),
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('another', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rel_another_set', to='m2m_through.employee')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_source_set', to='m2m_through.employee')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_target_set', to='m2m_through.employee')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='subordinates',
            field=models.ManyToManyField(through='m2m_through.Relationship', to='m2m_through.employee'),
        ),
        migrations.CreateModel(
            name='SymmetricalFriendship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_friended', models.DateField()),
                ('first', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='m2m_through.personselfrefm2m')),
                ('second', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='m2m_through.personselfrefm2m')),
            ],
        ),
        migrations.AddField(
            model_name='personselfrefm2m',
            name='sym_friends',
            field=models.ManyToManyField(through='m2m_through.SymmetricalFriendship', to='m2m_through.personselfrefm2m'),
        ),
        migrations.CreateModel(
            name='TestNoDefaultsOrNulls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nodefaultnonull', models.IntegerField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='m2m_through.group')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='m2m_through.person')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='nodefaultsnonulls',
            field=models.ManyToManyField(related_name='testnodefaultsnonulls', through='m2m_through.TestNoDefaultsOrNulls', to='m2m_through.person'),
        ),
    ]

# Generated by Django 5.0.2 on 2024-02-28 13:38

import django.db.models.deletion
import uuid
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
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('based_in_eu', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24)),
                ('assigned', models.DateField()),
                ('completed', models.DateField()),
                ('estimated_time', models.DurationField()),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('scalar', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'expressions_ExPeRiMeNt',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('integer', models.BigIntegerField(db_column='the_integer')),
                ('float', models.FloatField(db_column='the_float', null=True)),
                ('decimal_value', models.DecimalField(decimal_places=17, max_digits=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UUIDPK',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='RemoteEmployee',
            fields=[
                ('employee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='expressions.employee')),
                ('adjusted_salary', models.IntegerField()),
            ],
            bases=('expressions.employee',),
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('num_employees', models.PositiveIntegerField()),
                ('num_chairs', models.PositiveIntegerField()),
                ('based_in_eu', models.BooleanField(default=False)),
                ('ceo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_ceo_set', to='expressions.employee')),
                ('point_of_contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company_point_of_contact_set', to='expressions.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('secretary', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='managers', to='expressions.employee')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='expressions.manager'),
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_time', models.DateTimeField()),
                ('experiment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expressions.experiment')),
            ],
        ),
        migrations.CreateModel(
            name='SimulationRun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('midpoint', models.TimeField()),
                ('end', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='expressions.time')),
                ('start', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='expressions.time')),
            ],
        ),
        migrations.CreateModel(
            name='UUID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(null=True)),
                ('uuid_fk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='expressions.uuidpk')),
            ],
        ),
    ]

# Generated by Django 5.0.2 on 2024-03-19 21:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ManualPrimaryKey',
            fields=[
                ('primary_key', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_public', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='one_to_one.place')),
                ('serves_hot_dogs', models.BooleanField(default=False)),
                ('serves_pizza', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MultiModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('link2', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='one_to_one.manualprimarykey')),
                ('link1', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='one_to_one.place')),
            ],
        ),
        migrations.CreateModel(
            name='Bar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serves_cocktails', models.BooleanField(default=True)),
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='one_to_one.place')),
            ],
        ),
        migrations.CreateModel(
            name='Pointer',
            fields=[
                ('other', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='one_to_one.target')),
            ],
        ),
        migrations.CreateModel(
            name='ToFieldPointer',
            fields=[
                ('target', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='one_to_one.target', to_field='name')),
            ],
        ),
        migrations.CreateModel(
            name='HiddenPointer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='hidden+', to='one_to_one.target')),
            ],
        ),
        migrations.CreateModel(
            name='Pointer2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('other', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='second_pointer', to='one_to_one.target')),
            ],
        ),
        migrations.CreateModel(
            name='RelatedModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('link', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='one_to_one.manualprimarykey')),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_temp', models.BooleanField(default=False)),
                ('school', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='one_to_one.school')),
            ],
        ),
        migrations.CreateModel(
            name='UndergroundBar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serves_cocktails', models.BooleanField(default=True)),
                ('place', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='one_to_one.place')),
            ],
        ),
        migrations.CreateModel(
            name='Waiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='one_to_one.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('restaurants', models.ManyToManyField(to='one_to_one.restaurant')),
            ],
        ),
    ]

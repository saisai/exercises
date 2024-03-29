# Generated by Django 5.0.2 on 2024-02-27 14:14

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(default='Default headline', max_length=100)),
                ('pub_date', models.DateTimeField()),
            ],
            options={
                'ordering': ('pub_date', 'headline'),
            },
        ),
        migrations.CreateModel(
            name='PrimaryKeyWithDefault',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='PrimaryKeyWithDbDefault',
            fields=[
                ('uuid', models.IntegerField(db_default=1, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleSelectOnSave',
            fields=[
            ],
            options={
                'proxy': True,
                'select_on_save': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('basic.article',),
        ),
        migrations.CreateModel(
            name='ChildPrimaryKeyWithDefault',
            fields=[
                ('primarykeywithdefault_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='basic.primarykeywithdefault')),
            ],
            bases=('basic.primarykeywithdefault',),
        ),
        migrations.CreateModel(
            name='FeaturedArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='featured', to='basic.article')),
            ],
        ),
        migrations.CreateModel(
            name='SelfRef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='basic.article')),
                ('selfref', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='basic.selfref')),
            ],
        ),
    ]

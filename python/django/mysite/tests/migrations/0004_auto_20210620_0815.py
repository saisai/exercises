# Generated by Django 3.2 on 2021-06-20 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('tests', '0003_auto_20210310_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officialtag',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='officialtag',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='officialthroughmodel',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests_officialthroughmodel_tagged_items', to='contenttypes.contenttype', verbose_name='content type'),
        ),
        migrations.AlterField(
            model_name='officialthroughmodel',
            name='object_id',
            field=models.IntegerField(db_index=True, verbose_name='object ID'),
        ),
        migrations.AlterField(
            model_name='taggedcustompk',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests_taggedcustompk_tagged_items', to='contenttypes.contenttype', verbose_name='content type'),
        ),
        migrations.AlterField(
            model_name='throughgfk',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests_throughgfk_tagged_items', to='contenttypes.contenttype', verbose_name='content type'),
        ),
        migrations.AlterField(
            model_name='throughgfk',
            name='object_id',
            field=models.IntegerField(db_index=True, verbose_name='object ID'),
        ),
        migrations.AlterField(
            model_name='trackedtag',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='trackedtag',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='uuidtag',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='uuidtag',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='uuidtaggeditem',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests_uuidtaggeditem_tagged_items', to='contenttypes.contenttype', verbose_name='content type'),
        ),
        migrations.AlterField(
            model_name='uuidtaggeditem',
            name='object_id',
            field=models.UUIDField(db_index=True, verbose_name='object ID'),
        ),
    ]

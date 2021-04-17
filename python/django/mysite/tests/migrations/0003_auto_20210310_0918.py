# Generated by Django 3.1.7 on 2021-03-10 09:18

import django.db.models.deletion
from django.db import migrations, models

import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ("taggit", "0003_taggeditem_add_unique_index"),
        ("contenttypes", "0002_remove_content_type_name"),
        ("tests", "0002_auto_20200214_1129"),
    ]

    operations = [
        migrations.CreateModel(
            name="BaseFood",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="MultiInheritanceFood",
            fields=[
                (
                    "basefood_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="tests.basefood",
                    ),
                ),
            ],
            bases=("tests.basefood",),
        ),
        migrations.CreateModel(
            name="MultiInheritanceLazyResolutionFoodTag",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tests_multiinheritancelazyresolutionfoodtag_items",
                        to="taggit.tag",
                    ),
                ),
                (
                    "content_object",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tagged_items",
                        to="tests.multiinheritancefood",
                    ),
                ),
            ],
            options={
                "unique_together": {("content_object", "tag")},
            },
        ),
        migrations.AddField(
            model_name="multiinheritancefood",
            name="tags",
            field=taggit.managers.TaggableManager(
                help_text="A comma-separated list of tags.",
                through="tests.MultiInheritanceLazyResolutionFoodTag",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]

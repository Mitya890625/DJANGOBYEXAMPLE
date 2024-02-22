# Generated by Django 3.0 on 2024-01-26 12:56

import taggit.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("taggit", "0003_taggeditem_add_unique_index"),
        ("blog", "0002_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="tags",
            field=taggit.managers.TaggableManager(
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]
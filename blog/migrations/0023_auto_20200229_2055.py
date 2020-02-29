# Generated by Django 3.0.3 on 2020-02-29 23:55

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('blog', '0022_auto_20200229_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuracionbasica',
            name='hobbies',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Hobbies'),
        ),
    ]
# Generated by Django 2.2.6 on 2019-11-12 13:39

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_remove_informationtext_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='informationtext',
            name='text',
            field=tinymce.models.HTMLField(default='iug'),
            preserve_default=False,
        ),
    ]

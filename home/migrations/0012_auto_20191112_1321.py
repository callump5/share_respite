# Generated by Django 2.2.6 on 2019-11-12 13:21

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20191109_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homelandingtext',
            name='text',
            field=tinymce.models.HTMLField(),
        ),
    ]
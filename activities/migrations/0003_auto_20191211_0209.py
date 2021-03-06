# Generated by Django 2.2.6 on 2019-12-11 02:09

import activities.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_activity_slots'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityBlurb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'Activity Page Text',
                'verbose_name_plural': '1 - Activity Page Text',
            },
        ),
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name': 'Activity', 'verbose_name_plural': '2 - Activities'},
        ),
        migrations.RemoveField(
            model_name='activity',
            name='items',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='meeting',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='slots',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='title',
        ),
        migrations.AddField(
            model_name='activity',
            name='file',
            field=models.FileField(default='a', upload_to='', verbose_name=activities.models.upload_site_img),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity',
            name='date',
            field=models.DateField(),
        ),
    ]

# Generated by Django 2.2.6 on 2019-11-08 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('activity', models.TextField()),
                ('items', models.TextField()),
                ('meeting', models.TextField()),
            ],
            options={
                'verbose_name': 'Activity',
                'verbose_name_plural': '1 - Activities',
            },
        ),
    ]

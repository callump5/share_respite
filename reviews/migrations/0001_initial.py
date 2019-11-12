# Generated by Django 2.2.6 on 2019-11-09 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='anonymous', max_length=300)),
                ('review', models.TextField()),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': '1 - Reviews',
            },
        ),
    ]

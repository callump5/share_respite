# Generated by Django 2.2.6 on 2019-11-14 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contactrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactrequest',
            name='message',
            field=models.CharField(max_length=600),
        ),
    ]

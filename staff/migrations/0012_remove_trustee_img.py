# Generated by Django 2.2.6 on 2019-12-11 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0011_auto_20191211_0244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trustee',
            name='img',
        ),
    ]

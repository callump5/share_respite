# Generated by Django 2.2.6 on 2019-11-08 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_stickynote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stickynote',
            name='title',
            field=models.CharField(help_text='This will not be displayed, this is for your reference', max_length=300),
        ),
    ]

# Generated by Django 2.2.6 on 2019-11-08 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20191108_0226'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeAboutText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'About Text',
                'verbose_name_plural': 'About Text',
            },
        ),
    ]
# Generated by Django 2.2.6 on 2019-11-08 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PolicyCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Policy Category',
                'verbose_name_plural': '1 - Policy Categories',
            },
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='uploads')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policies.PolicyCategory')),
            ],
            options={
                'verbose_name': 'Policy',
                'verbose_name_plural': '2 - Policies',
            },
        ),
    ]

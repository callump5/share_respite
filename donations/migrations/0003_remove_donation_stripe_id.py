# Generated by Django 2.2.6 on 2019-11-12 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0002_donation_stripe_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='stripe_id',
        ),
    ]

# Generated by Django 2.2.6 on 2019-12-11 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0010_trustee_trusteesection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trustee',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.TrusteeSection'),
        ),
    ]

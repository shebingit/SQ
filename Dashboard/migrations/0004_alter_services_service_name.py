# Generated by Django 4.1 on 2022-08-11 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='service_name',
            field=models.CharField(max_length=60),
        ),
    ]

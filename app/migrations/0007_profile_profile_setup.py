# Generated by Django 3.2.16 on 2024-04-29 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20240429_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_setup',
            field=models.IntegerField(default=0),
        ),
    ]

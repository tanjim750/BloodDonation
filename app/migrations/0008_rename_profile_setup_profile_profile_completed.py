# Generated by Django 3.2.16 on 2024-04-29 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_profile_profile_setup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_setup',
            new_name='profile_completed',
        ),
    ]
# Generated by Django 3.2.16 on 2024-05-04 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_profile_under_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='under_review',
            new_name='is_under_review',
        ),
    ]
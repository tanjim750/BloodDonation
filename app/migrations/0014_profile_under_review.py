# Generated by Django 3.2.16 on 2024-05-04 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_rename_iamge_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='under_review',
            field=models.BooleanField(default=False),
        ),
    ]
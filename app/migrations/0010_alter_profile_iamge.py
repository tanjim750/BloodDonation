# Generated by Django 3.2.16 on 2024-04-29 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_profile_iamge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='iamge',
            field=models.FileField(default='profile/profile.png', upload_to='images/profiles'),
        ),
    ]

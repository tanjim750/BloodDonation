# Generated by Django 3.2.16 on 2024-05-08 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_homepage_fottertext'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='fotterText',
            new_name='footerText',
        ),
    ]

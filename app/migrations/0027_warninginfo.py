# Generated by Django 3.2.16 on 2024-05-09 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_auto_20240509_0603'),
    ]

    operations = [
        migrations.CreateModel(
            name='warningInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.TextField()),
                ('not_available', models.TextField()),
            ],
        ),
    ]

# Generated by Django 3.2.16 on 2024-05-08 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_rename_urgentnubmers_urgentnubmer'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headerText', models.CharField(max_length=100000)),
                ('title', models.CharField(max_length=1000000)),
                ('heading', models.CharField(max_length=10000)),
            ],
        ),
    ]

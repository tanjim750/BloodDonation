# Generated by Django 3.2.16 on 2024-05-08 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_alter_profile_last_donation'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonationAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('why_donations_need', models.TextField(blank=True, null=True)),
                ('details', models.TextField(blank=True, null=True)),
                ('account_type', models.CharField(max_length=10000)),
                ('address', models.TextField()),
            ],
        ),
    ]

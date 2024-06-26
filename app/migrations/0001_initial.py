# Generated by Django 3.2.16 on 2024-04-20 11:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Upazila',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upazila', models.CharField(max_length=1000)),
                ('discrict', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.district')),
            ],
        ),
        migrations.CreateModel(
            name='Unions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unions', models.CharField(max_length=1000)),
                ('upazila', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.upazila')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iamge', models.FileField(upload_to='profiles')),
                ('name', models.CharField(max_length=500)),
                ('is_donner', models.BooleanField(default=True)),
                ('non_donner_reason', models.CharField(blank=True, max_length=1000, null=True)),
                ('blood_group', models.CharField(max_length=500)),
                ('dob', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=500, null=True)),
                ('address', models.CharField(blank=True, max_length=10000, null=True)),
                ('document', models.FileField(blank=True, null=True, upload_to='documents')),
                ('face_verify', models.FileField(blank=True, null=True, upload_to='faces')),
                ('is_available', models.BooleanField(default=True)),
                ('last_donation', models.DateField(blank=True, null=True)),
                ('donated_before', models.BooleanField(default=False)),
                ('total_donation', models.IntegerField(default=0)),
                ('is_verified', models.BooleanField(default=False)),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.district')),
                ('unions', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.unions')),
                ('upazila', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.upazila')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

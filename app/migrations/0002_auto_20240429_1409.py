# Generated by Django 3.2.16 on 2024-04-29 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='blood_group',
            field=models.CharField(default='A+', max_length=1000),
        ),
        migrations.AlterField(
            model_name='profile',
            name='district',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.district'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='images/documents'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='face_verify',
            field=models.FileField(blank=True, null=True, upload_to='images/faces'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='unions',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.unions'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='upazila',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.upazila'),
        ),
    ]

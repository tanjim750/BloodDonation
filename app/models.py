from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class District(models.Model):
    district = models.CharField(max_length=1000)


class Upazila(models.Model):
    discrict = models.ForeignKey(District,on_delete=models.CASCADE)
    upazila = models.CharField(max_length=1000)


class Unions(models.Model):
    upazila = models.ForeignKey(Upazila,on_delete=models.CASCADE)
    unions = models.CharField(max_length=1000)


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    iamge = models.FileField(upload_to="profiles")
    name = models.CharField(max_length=500)
    is_donner = models.BooleanField(default=True)
    non_donner_reason = models.CharField(max_length=1000,null=True, blank=True)
    blood_group = models.CharField(max_length=500)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=500,null=True, blank=True)
    district = models.ForeignKey(District,on_delete=models.SET_NULL,null=True,blank=True)
    upazila = models.ForeignKey(Upazila,on_delete=models.SET_NULL,null=True,blank=True)
    unions = models.ForeignKey(Unions,on_delete=models.SET_NULL,null=True,blank=True)
    address = models.CharField(max_length=10000,null=True, blank=True)
    document = models.FileField(upload_to='documents',null=True, blank=True)
    face_verify = models.FileField(upload_to='faces',null=True, blank=True)
    is_available = models.BooleanField(default=True)
    last_donation = models.DateField(null=True, blank=True)
    donated_before = models.BooleanField(default=False)
    total_donation = models.IntegerField(default=0)
    is_verified = models.BooleanField(default=False)
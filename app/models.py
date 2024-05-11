from django.db import models
from django.contrib.auth.models import User


class HomePage(models.Model):
    header_text = models.CharField(max_length=100000)
    title = models.CharField(max_length=1000000)
    heading = models.CharField(max_length=10000)
    footer_text = models.CharField(max_length=10000, null=True)
    facebook_url = models.URLField(null=True,blank=True)
    twitter_url = models.URLField(null=True,blank=True)
    whatsapp_url = models.URLField(null=True,blank=True)
    google_url = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.heading


class warningInfo(models.Model):
    available = models.TextField()
    not_available = models.TextField()

    def __str__(self):
        return str(self.id)


class NotificationMail(models.Model):
    mail = models.CharField(max_length=10000)
    is_smtp = models.BooleanField(default=False)
    smtp_server = models.CharField(max_length=10000,null=True, blank=True)
    smtp_password = models.CharField(max_length=10000,null=True, blank=True)
    smtp_port = models.CharField(max_length=10000,null=True, blank=True)

    def __str__(self):
        return self.mail
    

class NonDonnerReason(models.Model):
    reason = models.TextField()
    value = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.reason)
    
class BloodGroup(models.Model):
    name = models.CharField(max_length=1000)
    symbol = models.TextField()
    image = models.ImageField(upload_to='images/blood')

    def __str__(self):
        return self.name

class District(models.Model):
    district = models.CharField(max_length=1000)

    def __str__(self):
        return self.district


class Upazila(models.Model):
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    upazila = models.CharField(max_length=1000)

    def __str__(self):
        return self.upazila


class Unions(models.Model):
    upazila = models.ForeignKey(Upazila,on_delete=models.CASCADE)
    unions = models.CharField(max_length=1000)

    def __str__(self):
        return self.unions


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    image = models.FileField(upload_to="images/profiles",default='images/profiles/profile.png')
    non_donner_reason = models.CharField(max_length=1000,null=True, blank=True)
    blood_group = models.ForeignKey(BloodGroup,on_delete=models.SET_NULL,null=True)
    dob = models.DateField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=500,null=True, blank=True)
    district = models.ForeignKey(District,on_delete=models.SET_NULL,null=True,blank=True)
    upazila = models.ForeignKey(Upazila,on_delete=models.SET_NULL,null=True,blank=True)
    unions = models.ForeignKey(Unions,on_delete=models.SET_NULL,null=True,blank=True)
    address = models.CharField(max_length=10000,null=True, blank=True)
    document = models.FileField(upload_to='images/documents',null=True, blank=True)
    face_verify = models.FileField(upload_to='images/faces',null=True, blank=True)
    last_donation = models.DateField(null=True, blank=True)
    total_donation = models.IntegerField(default=0)
    profile_completed = models.IntegerField(default=0) # percentage of profile completed
    donated_before = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    is_donner = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_under_review = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.username)


class DonationAccount(models.Model):
    why_donations_need = models.TextField(null=True, blank=True)
    details = models.TextField(blank=True,null=True)
    account_type = models.CharField(max_length=10000)
    address = models.TextField()

    def __str__(self):
        return str(self.account_type)


class UrgentNubmersZone(models.Model):
    zone = models.CharField(max_length=10000)

    def __str__(self):
        return str(self.zone)

class UrgentNubmer(models.Model):
    zone = models.ForeignKey(UrgentNubmersZone, on_delete=models.CASCADE)
    name = models.CharField(max_length=10000)
    number = models.TextField()

    def __str__(self):
        return str(self.zone.zone)
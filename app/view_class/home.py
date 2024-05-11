from django.shortcuts import render
from app.models import *

class Home:
    def get(self, request):
        blood_group = BloodGroup.objects.all()
        blood_group = [blood_group[0:3], blood_group[3:6], blood_group[6:]]
        donation_account = DonationAccount.objects.all()
        urgent_numbers = UrgentNubmersZone.objects.all()
        home_page = HomePage.objects.first()

        context = {
            "blood_group": blood_group,
            "donation_account": donation_account,
            "urgent_numbers" : urgent_numbers,
            "home_page": home_page
        }
        return render(request, 'home.html',context)
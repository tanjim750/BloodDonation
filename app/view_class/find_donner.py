from django.shortcuts import render, redirect
from app.models import *

class FindDonner:
    def get(self, request, *args, **kwargs):
        district = District.objects.all()
        upazila = Upazila.objects.all()
        unions = Unions.objects.all()
        # print(district.first().upazila_set.all())
        blood_group = request.GET.get('group',None)
        warning = warningInfo.objects.first()

        
        context = {
            "district": district,
            'upazila': upazila,
            "unions": unions,
            'warning': warning
            
        }

        if blood_group:
            donners = Profile.objects.filter(blood_group__id = blood_group, is_verified = True,
                                            is_donner = True,is_available=True)
            context["donners"] = donners

        return render(request, 'donner.html',context)
    
    def post(self, request, *args, **kwargs):
        district = District.objects.all()
        upazila = Upazila.objects.all()
        unions = Unions.objects.all()
        warning = warningInfo.objects.first()

        context = {
            "district": district,
            'upazila': upazila,
            "unions": unions,
            'warning': warning
        }

        selected_district = request.POST.get('district',None)
        selected_upazila = request.POST.get('upazila',None)
        selected_union = request.POST.get('unions',None)
        blood_group = request.GET.get('group',None)

        if selected_district and selected_upazila and selected_union and blood_group:
            donners = Profile.objects.filter(blood_group__id = blood_group,district__district = selected_district, upazila__upazila = selected_upazila,
                                            unions__unions = selected_union,is_verified = True,
                                            is_donner = True,is_available=True)
            
            context["donners"] = donners
            context["selected_district"] = selected_district
            context["selected_upazila"] = selected_upazila
            context["selected_union"] = selected_union
        else:
            context.update({'status':401,'error':"Missing required credentials."})

        return render(request, 'donner.html',context)
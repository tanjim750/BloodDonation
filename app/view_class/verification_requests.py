from django.shortcuts import render, redirect
from django.urls import reverse

from app.models import Profile

class VerificationRequests:
    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            profiles = Profile.objects.filter(is_under_review=True,is_verified=False)
            admin_url = admin_url = request.build_absolute_uri(reverse('admin:index')) 

            context = {
                "profiles": profiles,
                "admin_url": admin_url
            }
            return render(request, 'verification-requests.html',context)
        else:
            return render(request, '404.html')
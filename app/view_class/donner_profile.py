from django.shortcuts import render, redirect
from django.http import HttpResponse

from app.models import *

class DonnerProfile:
    def get(self, request, *args, **kwargs):
        username = request.GET.get('user',None)
        context = {}

        if username:
            profile = Profile.objects.get(user__username=username)
            context['profile'] = profile
        else:
            return HttpResponse("Unknown request. Please try again")

        return render(request, 'donner-profile.html',context)
    
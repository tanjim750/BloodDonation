from django.shortcuts import render, redirect
import datetime

class Profile:
    def get(self, request, *args, **kwargs):
        today = datetime.datetime.today().date()
        last_donation = request.user.profile.last_donation
        if last_donation:
            last_donation = (today - last_donation).days

        context = {
            'last_donation': last_donation,
        }
        return render(request, 'user-profile.html',context)
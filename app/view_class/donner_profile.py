from django.shortcuts import render, redirect

class DonnerProfile:
    def get(self, request, *args, **kwargs):
        return render(request, 'donner-profile.html')
    
    def post(self, request, *args, **kwargs):
        return render(request, 'donner-profile.html')
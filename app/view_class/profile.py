from django.shortcuts import render, redirect

class Profile:
    def get(self, request, *args, **kwargs):
        return render(request, 'user-profile.html')
    
    def post(self, request, *args, **kwargs):
        return render(request, 'user-profile.html')
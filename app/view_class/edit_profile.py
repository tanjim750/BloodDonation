from django.shortcuts import render, redirect

class EditProfile:
    def get(self, request, *args, **kwargs):
        return render(request, 'edit-profile.html')
    
    def post(self, request, *args, **kwargs):
        return render(request, 'edit-profile.html')
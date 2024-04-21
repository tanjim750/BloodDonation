from django.shortcuts import render, redirect

class ChangePassword:
    def get(self, request, *args, **kwargs):
        return render(request, 'change-pass.html')
    
    def post(self, request, *args, **kwargs):
        return render(request, 'change-pass.html')
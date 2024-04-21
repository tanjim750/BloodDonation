from django.shortcuts import render, redirect

class FindDonner:
    def get(self, request, *args, **kwargs):
        return render(request, 'donner.html')
    
    def post(self, request, *args, **kwargs):
        return render(request, 'donner.html')
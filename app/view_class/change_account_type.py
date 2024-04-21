from django.shortcuts import render, redirect

class ChangeAccountType:
    def get(self, request, *args, **kwargs):
        return render(request, 'change-account-type.html')
    
    def post(self, request, *args, **kwargs):
        return render(request, 'change-account-type.html')
from django.shortcuts import render, redirect
from app.models import *

class ChangeAccountType:
    def get(self, request, *args, **kwargs):
        return render(request, 'change-account-type.html')
    
    def post(self, request, *args, **kwargs):
        account_type = request.POST.get('account-type', None)

        if account_type == "donner":
            profile = Profile.objects.get(user=request.user)
            profile.is_donner = True
            profile.save()
            return redirect('edit-profile')
        
        return render(request, 'change-account-type.html')
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class ChangePassword:
    def get(self, request, *args, **kwargs):
        return render(request, 'change-pass.html')
    
    def post(self, request, *args, **kwargs):
        crnt_pass = request.POST.get('crnt_pass',None)
        new_pass = request.POST.get('new_pass',None)
        print(crnt_pass,new_pass)

        if crnt_pass and new_pass:
            if len(new_pass) >= 6:
                username = request.user.username
                user = User.objects.get(username=username)
                print(user.password)
                auth =  authenticate(request, username=username, password=crnt_pass)

                if auth is not None:
                    user.set_password(new_pass)
                    user.save()
                    auth =  authenticate(request, username=username, password=new_pass)
                    login(request,auth)

                    context = {'status': 200,'success': 'Your password has been changed successfully'}
                else:
                    context = {'status': 403,'error': 'Invalid current password'}
            else:
                context = {'status':403,'error':"Password length must be at least 6."}
        else:
            context = {'status': 401,'error': 'Missing required credentials'}

        return render(request, 'change-pass.html',context)
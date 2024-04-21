from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from app.models import *

class Register:
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'register.html')
        else:
            return redirect('home')
    
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home') # for security reasons
        
        # main actions
        name = request.POST.get('name', None)
        blood_group = request.POST.get('blood_group', None)
        username:str = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        account_type:str = request.POST.get('account_type', None)
        non_donner_reason = request.POST.get('non_donner_reason', None)

        print(name,username, email, password, account_type, non_donner_reason)
        if username:
            is_exists = User.objects.filter(username=username).exists()
            if is_exists:
                context = {'status':403,'error':"Number Or Email Address already exists."}
                return render(request,'register.html', context)
            else:
                if name and blood_group and password and account_type:
                    if len(password) < 8:
                        context = {'status':403,'error':"Password length must be at least 8."}
                        return render(request,'register.html', context)
                    
                    if len(username) != 11:

                        context = {'status':403,'error':"Please Use a valid Number"}
                        return render(request,'register.html', context)
                    else:
                        if (not username.startswith('016') or 
                                not username.startswith('015') or not username.startswith('019') or 
                                not username.startswith('014') or not username.startswith('018') or
                                not username.startswith('017')):
                            
                            context = {'status':403,'error':"Please Use a valid Number"}
                            return render(request,'register.html', context)
                    
                    if account_type == 'non-donner' and non_donner_reason is None:
                        context = {'status':401,'error':"Missing required credentials. ddd"}
                        return render(request,'register.html', context)
                    else:
                        is_donner = False if account_type.lower() == 'non-donner' else True

                        user = User.objects.create_user(
                            username=username,
                            email=email,
                            password=password,
                        )
                        Profile.objects.create(
                            user=user,
                            name = name,
                            blood_group = blood_group,
                            is_donner = is_donner,
                            non_donner_reason = non_donner_reason
                        )

                        # login user
                        auth = authenticate(request,username=username,password=password)
                        if auth is not None:
                            login(request,auth)
                        
                        return redirect('edit-profile')


                else:
                    context = {'status':401,'error':"Missing required credentials. other"}
                    return render(request,'register.html', context)

        else:
            context = {'status':401,'error':"Missing required credentials. username"}
            return render(request,'register.html', context)

from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from app.models import *

class Register:
    def __init__(self):
        self.valid_num = ["014","015","016","017","018","019"]

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            blood_groups = BloodGroup.objects.all().order_by('symbol')
            non_donner_reasons = NonDonnerReason.objects.all()

            context = {
                'blood_groups': blood_groups,
                'non_donner_reasons': non_donner_reasons
            }
            return render(request, 'register.html',context)
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

        blood_groups = BloodGroup.objects.all().order_by('symbol')
        non_donner_reasons = NonDonnerReason.objects.all()

        context = {
                'blood_groups': blood_groups,
                'non_donner_reasons': non_donner_reasons
            }
        
        # print(name,username, email, password, account_type, non_donner_reason)
        if username:
            if not email:
                is_exists = User.objects.filter(username=username).exists()
                error = "Number already exists."
            else:
                is_exists = User.objects.filter(Q(username=username) | Q(email=email) | Q(username=username, email=email)).exists()
                error = "Number Or Email Address already exists."

            if is_exists:
                context.update({'status':403,'error':error})
                return render(request,'register.html', context)
            else:
                if name and blood_group and password and account_type:
                    if len(password) < 6:
                        context.update({'status':403,'error':"Password length must be at least 6."})
                        return render(request,'register.html', context)
                    
                    if len(username) != 11 and username[2] not in self.valid_num:

                        context.update({'status':403,'error':"Please Use a valid Number."})
                        return render(request,'register.html', context)
                    
                    if account_type == 'non-donner' and non_donner_reason is None:
                        context.update({'status':401,'error':"Missing required credentials."})
                        return render(request,'register.html', context)
                    else:
                        is_donner = False if account_type.lower() == 'non-donner' else True
                        
                        completed = 3*6.67 # profile completed point '3'(name,blood_group,is_donner)

                        user = User.objects.create_user(
                            username=username,
                            email=email,
                            password=password,
                        )

                        Profile.objects.create(
                            user=user,
                            name = name,
                            blood_group = BloodGroup.objects.filter(id=blood_group).first(),
                            is_donner = is_donner,
                            non_donner_reason = non_donner_reason,
                            profile_completed = completed
                        )

                        # login user
                        auth = authenticate(request,username=username,password=password)
                        if auth is not None:
                            login(request,auth)

                        if user.profile.is_donner:
                            return redirect('edit-profile')
                        else:
                            return redirect('home')


                else:
                    context.update({'status':401,'error':"Missing required credentials."})
                    return render(request,'register.html', context)

        else:
            context.update({'status':401,'error':"Missing required credentials. username"})
            return render(request,'register.html', context)

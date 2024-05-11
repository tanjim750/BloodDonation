from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

# import views classes
from . import view_class
from .models import *

    

def redirect_to_editpage(request):
    user = request.user
    completed = user.profile.profile_completed
    is_donner = user.profile.is_donner

    if is_donner and completed < 50:
        return redirect('edit-profile')
    else:
        return None
    
    
@method_decorator(login_required, name='dispatch')
class RedirectToHome(View):
    def get(self, request, *args, **kwargs):
        return redirect('home')


@method_decorator(login_required, name='dispatch')
class Home(View):
    def __init__(self):
        self.obj = view_class.Home()
    
    def get(self, request):
        check = redirect_to_editpage(request)
        if check is not None:
            return check
        
        response = self.obj.get(request)
        return response


class Login(View):
    def __init__(self):
        self.obj = view_class.Login()
    
    def get(self, request):
        response = self.obj.get(request)
        return response
    
    def post(self, request):
        response = self.obj.post(request)
        return response

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class Register(View):
    def __init__(self):
        self.obj = view_class.Register()
    
    def get(self, request):
        response = self.obj.get(request)
        return response
    
    def post(self, request):
        response = self.obj.post(request)
        return response

@method_decorator(login_required, name='dispatch')
class FindDonner(View):
    def __init__(self):
        self.obj = view_class.FindDonner()
    
    def get(self, request):
        check = redirect_to_editpage(request)
        if check is not None:
            return check
        
        response = self.obj.get(request)
        return response
    
    def post(self, request):
        response = self.obj.post(request)
        return response

@method_decorator(login_required, name='dispatch')
class DonnerProfile(View):
    def __init__(self):
        self.obj = view_class.DonnerProfile()
    
    def get(self, request):
        check = redirect_to_editpage(request)
        if check is not None:
            return check
        
        response = self.obj.get(request)
        return response
    
    def post(self, request):
        response = self.obj.post(request)
        return response

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def __init__(self):
        self.obj = view_class.Profile()
    
    def get(self, request):
        check = redirect_to_editpage(request)
        if check is not None:
            return check
        
        response = self.obj.get(request)
        return response
    
    def post(self, request):
        response = self.obj.post(request)
        return response
    
@method_decorator(login_required, name='dispatch')
class EditProfile(View):
    def __init__(self):
        self.obj = view_class.EditProfile()
    
    def get(self, request):
        response = self.obj.get(request)
        return response
    
    def post(self, request):
        response = self.obj.post(request)
        return response
    
@method_decorator(login_required, name='dispatch')
class ChangePassword(View):
    def __init__(self):
        self.obj = view_class.ChangePassword()
    
    def get(self, request):
        check = redirect_to_editpage(request)
        if check is not None:
            return check
        
        response = self.obj.get(request)
        return response
    
    def post(self, request):
        response = self.obj.post(request)
        return response
    
@method_decorator(login_required, name='dispatch')
class ChangeAccountType(View):
    def __init__(self):
        self.obj = view_class.ChangeAccountType()
    
    def get(self, request):
        response = self.obj.get(request)
        return response
    
    def post(self, request):
        response = self.obj.post(request)
        return response

@method_decorator(login_required, name='dispatch')
class ChangeAvailableStatusApi(View):
    def get(self, request):
        user = User.objects.filter(username=request.user.username).first()
        profile = Profile.objects.filter(user=user).first()

        if profile.is_available:
            profile.is_available = False
        else:
            profile.is_available = True

        profile.save()
        return JsonResponse({'status':200,'is_available': profile.is_available})

@method_decorator(login_required, name='dispatch')
class VerificationRequests(View):
    def __init__(self):
        self.obj = view_class.VerificationRequests()

    def get(self, request):
        response = self.obj.get(request)
        return response
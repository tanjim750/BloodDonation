from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

# import views classes
from . import view_class

@method_decorator(login_required, name='dispatch')
class RedirectToHome(View):
    def get(self, request, *args, **kwargs):
        return render(request,'index.html')

@method_decorator(login_required, name='dispatch')
class Home(View):
    def __init__(self):
        self.obj = view_class.Home()
    
    def get(self, request):
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
        response = self.obj.get(request)
        return response
    
    def post(self, request):
        response = self.obj.post(request)
        return response

@method_decorator(login_required, name='dispatch')
class Profile(View):
    def __init__(self):
        self.obj = view_class.Profile()
    
    def get(self, request):
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
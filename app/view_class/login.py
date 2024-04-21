from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


class Login:
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'login.html')
        else:
            return redirect('home')
    
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request) # for security reasons
        
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        
        if username and password:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            
            else:
                context = {'status': 403,'error': 'Invalid username or password'}
        else:
            context = {'status': 401,'error': 'Missing login credentials'}

        return render(request, 'login.html',context=context)


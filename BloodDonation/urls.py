"""BloodDonation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.RedirectToHome.as_view(), name='index'),
    path('home/', views.Home.as_view(), name='home'),
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('find-donner/', views.FindDonner.as_view(), name='find-donner'),
    path('donner-profile/', views.DonnerProfile.as_view(), name='donner-profile'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('edit-profile/', views.EditProfile.as_view(), name='edit-profile'),
    path('change-password/', views.ChangePassword.as_view(), name='change-password'),
    path('change-account-type/', views.ChangeAccountType.as_view(), name='change-account-type'),
]

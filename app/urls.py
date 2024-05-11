from django.urls import path
from . import views

urlpatterns = [
    path('', views.RedirectToHome.as_view(), name='index'),
    path('home/', views.Home.as_view(), name='home'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('register/', views.Register.as_view(), name='register'),
    path('find-donner/', views.FindDonner.as_view(), name='find-donner'),
    path('donner-profile/', views.DonnerProfile.as_view(), name='donner-profile'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('edit-profile/', views.EditProfile.as_view(), name='edit-profile'),
    path('change-password/', views.ChangePassword.as_view(), name='change-password'),
    path('change-account-type/', views.ChangeAccountType.as_view(), name='change-account-type'),
    path('api/change-available-status/',views.ChangeAvailableStatusApi.as_view(), name='change-available-status'),
    path('verification-requests/', views.VerificationRequests.as_view(), name='verification-requests'),
]
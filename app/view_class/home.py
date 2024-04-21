from django.shortcuts import render

class Home:
    def get(self, request):
        return render(request, 'home.html')
from django.views import View
from django.shortcuts import redirect,render
from django.contrib.auth import logout as auth_logout

class logoutView(View):
    def get(self,request):
        auth_logout(request)
        return redirect('login')
    

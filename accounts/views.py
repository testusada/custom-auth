from django.shortcuts import render,redirect

from allauth.account import views
from django.urls.base import clear_script_prefix
# Create your views here.

class LoginView(views.LoginView):
    template_name = 'accounts/login.html'

class LogoutView(views.LogoutView):
    template_name='accounts/logout.html'

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            self.logout()
        return redirect('/')

class SignupView(views.SignupView):
    template_name = 'accounts/signup.html'

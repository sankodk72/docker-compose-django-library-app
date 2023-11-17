from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from authentication.models import CustomUser


def index(req):
    return render(req, 'authentication/index.html')


def logoutUSER(req):
    logout(req)
    return redirect('log')

class LoginUser(LoginView):
    template_name = 'authentication/login.html'
    form_class = AuthenticationForm
    def get_success_url(self):
        return reverse_lazy('main')


def register(req):
    if req.method == 'POST':
        mail = req.POST.get('uemail')
        password = req.POST.get('new_pass')
        name = req.POST.get('uname')
        if req.POST.get('is_super'):
            CustomUser.objects.create_superuser(email=mail, password=password, first_name=name)
        else:
            CustomUser.objects.create_user(email=mail, password=password, first_name=name)
        return redirect('log')
    return render(req, 'authentication/register.html')

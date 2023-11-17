from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from authentication.models import CustomUser


def index(req):
    return HttpResponse('<h1>Users app</h1>')

@login_required(login_url='/authentication/login')
def all_users(req):

    if not req.user.role:
        return redirect('index')

    all_users_data = CustomUser.objects.all()
    return render(req, 'user/all_users.html', context={'users': all_users_data})


def spec_user(req, user_id):
    spec_user = CustomUser.objects.get(id=user_id)
    return render(req, 'user/specific_user.html', context={'user': spec_user})
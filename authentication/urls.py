from django.urls import path
from . import views

urlpatterns = [
    path('login', views.LoginUser.as_view(), name='log'),
    path('register', views.register, name='reg'),
    path('logout', views.logoutUSER, name='logout'),
    path('', views.index, name='main')
]
from django.urls import path
from user import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_users/', views.all_users, name='all_users'),
    path('<int:user_id>', views.spec_user, name='view_user'),
]
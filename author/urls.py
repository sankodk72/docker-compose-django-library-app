from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('info', views.info, name='info'),
    path('add', views.addAuthor, name='add'),
    path('delete', views.deleteAuthor, name='del'),
    path('add/', views.add_author, name='add_author'),
    path('edit/<int:author_id>/', views.edit_author, name='edit_author')
]
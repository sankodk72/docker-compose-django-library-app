from django.urls import path
from . import views


urlpatterns = [
    path('all-books', views.show_all, name='allbooks'),
    path('<int:book_id>', views.view_book, name='view_book'),
    path('filter-books', views.filter_books, name='filter_books'),
    path('add/', views.add_book, name='add_book'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book')
]
from django.urls import path
from order import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create_order/', views.create_order, name='crt'),
    path('all_orders/', views.all_orders, name='allord'),
    path('my_orders/', views.user_orders, name='u_ord'),
    path('close/', views.close_order, name='cls')
]

'<book_id:int>'
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from order.models import Order
from book.models import Book


@login_required(login_url='/authentication/login')
def all_orders(req):
    if not req.user.role:
        return redirect('index')
    data = Order.objects.filter(end_at=None)
    return render(req, 'order/all_orders.html', context={'orders': data})


@login_required(login_url='/authentication/login')
def create_order(req):
    all_books = Book.objects.all()
    if req.method == 'POST':
        Order.objects.create(book=Book.objects.get(id=req.POST.get('book')), user=req.user)
    return render(req, 'order/create_new_order.html', context={'books': all_books})


def index(req):
    return HttpResponse('<h1>Order app</h1>')


@login_required(login_url='/authentication/login')
def user_orders(req):
    # if req.user.role:
    #     return redirect('index')
    data = Order.objects.filter(user=req.user)
    return render(req, 'order/user_orders.html', context={'orders': data})


@login_required(login_url='/authentication/login')
def close_order(req):
    if not req.user.role:
        return redirect('index')
    data = Order.objects.filter(end_at=None)
    if req.method == 'POST':
        for key in req.POST:
            if key != 'csrfmiddlewaretoken':
                order = Order.objects.get(id=key)
                order.update(end_at=timezone.now())
        return redirect('index')
    return render(req, 'order/close_order.html', context={'orders': data})
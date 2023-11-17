from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import AuthorForm
from .models import *
# from django.http import HttpResponseRedirect
# from django.urls import reverse


def index(req):
    return HttpResponse('<h1>Authors app</h1>')


@login_required(login_url='/authentication/login')
def info(req):
    if not req.user.role:
        return redirect('index')

    data = Author.objects.all().values()
    for item in data:
        item.update({'books': Author.objects.get(id=item['id']).authorof.all()})

    return render(req, 'author/all_authors.html', context={'data_abt_authors': data})


@login_required(login_url='/authentication/login')
def addAuthor(req):

    if not req.user.role:
        return redirect('index')

    if req.method == 'POST':
        auth_name = req.POST.get('authorname')
        auth_sname = req.POST.get('authorsurname')
        auth_patr = req.POST.get('authorpatr')
        Author.objects.create(name=auth_name, surname=auth_sname, patronymic=auth_patr)

    return render(req, 'author/add_author.html')

@login_required(login_url='/authentication/login')
def deleteAuthor(req):

    pull = []
    for item in list(Author.objects.all()):
        if not item.authorof.all():
            pull.append(item)

    if req.method == 'POST':
        for item in req.POST:
            Author.objects.filter(name=item).delete()
        return redirect('info')

    return render(req, 'author/delete_author.html', context={'authors': pull})


#######Forms#######

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            #return HttpResponseRedirect(reverse('info'))
            return redirect('info')  # Replace 'author_list' with the URL name for the author list view
    else:
        form = AuthorForm()
    return render(request, 'author/form_add_author.html', {'form': form})

def edit_author(request, author_id):
    author = Author.objects.get(pk=author_id)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            #return HttpResponseRedirect(reverse('info'))
            return redirect('info')  # Replace 'author_list' with the URL name for the author list view
    else:
        form = AuthorForm(instance=author)
    return render(request, 'author/form_edit_author.html', {'form': form, 'author': author})

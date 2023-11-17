#from django.http import HttpResponse
from django.shortcuts import render, redirect
#from book.models import Book
from .forms import BookForm
from .models import Book


def show_all(req):
    all_books_data = Book.objects.all()

    return render(req, 'book/showbooks.html', context={'books': all_books_data})


def view_book(req, book_id):
    book = Book.objects.get(id=book_id)
    return render(req, 'book/view_book.html', context={'book': book})


def filter_books(req):
    author_filter = req.GET.get('authorid', '')
    book_name_filter = req.GET.get('book_name', '')
    book_by_author, book_by_name = None, None

    if author_filter:
        book_by_author = Book.objects.filter(author_id=author_filter)
    if book_name_filter:
        book_by_name = Book.objects.filter(slug_link=book_name_filter)

    return render(req, 'book/filter_books.html', context={'filter_by_author': book_by_author, 'filter_by_name': book_by_name})

#####Forms#####

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all-books')  # Replace 'book_list' with the URL name for the book list view
    else:
        form = BookForm()
    return render(request, 'book/add_book.html', {'form': form})

def edit_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('all-books')  # Replace 'book_list' with the URL name for the book list view
    else:
        form = BookForm(instance=book)
    return render(request, 'book/edit_book.html', {'form': form, 'book': book})

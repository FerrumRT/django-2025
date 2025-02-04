from django.shortcuts import render

from book.models import Book


# Create your views here.
def index(request):
    if request.method == 'GET':
        books = Book.objects.all()
        context = {'books': books}
        return render(request, "book/index.html", context)


# Create your views here.
def book(request, book_id):
    if request.method == 'GET':
        b = Book.objects.get(pk=book_id)
        context = {'my_book': b}
        return render(request, "book/book.html", context)

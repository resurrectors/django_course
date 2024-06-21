from django.shortcuts import render
from . import views
from .models import Book, Author
# Create your views here.


def index(request):
    authors = Author.objects.all()
    books = Book.objects.all()
    num_books = books.count()
    return render(request, "book_store/books.html", {
        "total_no_of_books": num_books,
        "books": books,
        "authors": authors
    })

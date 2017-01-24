from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Book, Review
# Create your views here.
def index(request):
    pass

def show(request):
    pass

def add(request):
    return render(request, 'books/new.html')

def create(request):
    if request.method == "POST":
        book_created = Book.objects.create_book(request)
        if book_created:
            review_created = Review.objects.create_review(request)
    return redirect(reverse('books:create'))

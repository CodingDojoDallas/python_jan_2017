from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import Book, Review

# Create your views here.
def index(request):
    # books = Book.objects.all().order_by('-created_at')[:3]
    books = Book.objects.all().order_by('-review__created_at')[:3]
    context = {'books': books}
    return render(request, 'books/index.html', context)

def show(request, id):
    book = Book.objects.get(id=id)
    context = {
        'book': book
    }
    return render(request, 'books/show.html', context)

def new_book(request):
    books = Book.objects.values('author').distinct()
    context = {'books': books}
    return render(request, 'books/new.html', context)

def new_review(request):
    book_obj = Book.objects.get(id=request.POST['book_id'])
    did_create = Review.objects.create_review(request, book_obj)
    if did_create:
        return redirect(reverse("books:index"))
    else:
        return HttpResponse("Something went wrong")

def create(request):
    book_obj = Book.objects.create_book(request)
    if book_obj:
        Review.objects.create_review(request, book_obj)
    return redirect(reverse("books:index"))

def edit(request, id):
    return render(request, 'books/edit.html')

def delete(request, id):
    return redirect(reverse("books:index"))

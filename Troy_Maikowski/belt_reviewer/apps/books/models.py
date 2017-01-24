from __future__ import unicode_literals

from django.db import models
from django.contrib import messages

# Create your models here.
class BookManager(models.Manager):
    def create_book(self, request):
        errors = {
            'errors': []
        }
        if not request.POST['title']:
            msg = "Please provide a title"
            errors['errors'].append(msg)
        if request.POST['existing_author'] == 'None' and not request.POST['new_author']:
            msg = "Please provide an existing or new author"
            errors['errors'].append(msg)
        if not errors['errors']:
            if request.POST['existing_author']:
                book = Book(
                    title=request.POST['title'],
                    author=request.POST['existing_author']
                )
                book.save()
            else:
                book = Book(
                    title=request.POST['title'],
                    author=request.POST['new_author']
                )
                book.save()
            return book
        else:
            for msg in messages:
                messages.error(request, msg)
            return False

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

class ReviewManager(models.Manager):
    def create_review(self, request, book_obj=None):
        content = request.POST['review_content']
        rating = request.POST['rating']
        errors = {
            'errors': []
        }
        if not content:
            msg = "Please provide review content"
            errors['errors'].append(msg)
        if not rating:
            msg = "Please provide a rating"
            errors['errors'].append(msg)
        if int(rating) < 1 or int(rating) > 5:
            msg = "Please enter a number between 1 and 5"
            errors['errors'].append(msg)
        if errors['errors']:
            for msg in errors['errors']:
                messages.error(request, msg)
            return False
        else:
            Review.objects.create(
                content=content,
                rating=rating,
                book=book_obj
            )
            return True

class Review(models.Model):
    content = models.TextField()
    rating = models.PositiveSmallIntegerField()
    book = models.ForeignKey(Book)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()

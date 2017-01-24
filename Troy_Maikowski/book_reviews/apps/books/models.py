from __future__ import unicode_literals

from django.db import models
from django.contrib import messages

# Create your models here.
class BookManager(models.Manager):
    def create_book(self, request):
        existing_author = request.POST['existing_author']
        new_author = request.POST['new_author']
        if len(request.POST['title']) > 0:
            if existing_author == '0' and new_author:
                Book(
                    name=request.POST['title'],
                    author=new_author
                ).save()
            elif existing_author != 0 and not new_author:
                Book(
                    name=request.POST['title'],
                    author=existing_author
                ).save()
            else:
                msg = "Please either select an existing author or new author"
                messages.error(request, msg)
                return False
            return True
        return False

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

class ReviewManager(models.Manager):
    def create_review(self, request):
        errors = {
            'errors': []
        }
        if len(request.POST['review_body']) == 0 and request.POST['rating']:
            msg = "A review must have content and a rating, not either-or."
            errors['errors'].append(msg)
        if len(request.POST['review_body']) > 0 and not request.POST['rating']:
            msg = "A review must have content and a rating, not either-or."
            errors['errors'].append(msg)
        if request.POST['rating'] < 1 or request.POST['rating'] > 5:
            msg = "Rating must be between 1 and 5 stars"
            errors['errors'].append(msg)
        if errors['errors']:
            return errors
        else:
            return True

class Review(models.Model):
    content = models.TextField(max_length=1000)
    book = models.ForeignKey(Book)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()

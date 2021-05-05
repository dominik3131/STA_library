from django.db import models
from datetime import datetime    

class Author(models.Model):
    first_name = models.CharField(max_length=100, )
    last_name = models.CharField(max_length=100)

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

class Genre(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20)
    authors = models.ManyToManyField(Author)
    genres = models.ManyToManyField(Genre)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)

class BookCopy(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    copy_number = models.IntegerField()

class UserCard(models.Model):
    #TODO user who is owner of card
    join_date = models.DateTimeField(default=datetime.now, blank=True)

class Borrowing(models.Model):
    user_card = models.ForeignKey(UserCard, on_delete=models.CASCADE)
    book_copy = models.ForeignKey(BookCopy, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(default=datetime.now, blank=True)
    return_date = models.DateTimeField(blank=True)
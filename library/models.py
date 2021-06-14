from django.db import models
from datetime import datetime    
from django.contrib.auth.models import User, UserManager

class AdminManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(is_staff=True)

class Admin(User):
    objects = AdminManager()

    class Meta:
        proxy = True
        ordering = ('first_name', )

    def save(self, *args, **kwargs):
        self.is_staff = True
        self.is_superuser = True
        return super(Admin, self).save(*args, **kwargs)

class ReaderManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(is_staff=False)

class Reader(User):
    objects = ReaderManager()

    class Meta:
        proxy = True
        ordering = ('first_name', )

    def save(self, *args, **kwargs):
        self.is_staff = False
        self.is_superuser = False
        return super(Reader, self).save(*args, **kwargs)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
            return self.first_name + ' ' + self.last_name

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
            return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
            return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20)
    authors = models.ManyToManyField(Author)
    genres = models.ManyToManyField(Genre)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)

    def __str__(self):
            return self.title + ' - ' + str(self.authors)

class BookCopy(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    copy_number = models.IntegerField()

    def __str__(self):
            return str(self.book) + ' (' + str(self.copy_number) +')'

class Borrowing(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book_copy = models.ForeignKey(BookCopy, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(default=datetime.now, blank=True)
    return_date = models.DateTimeField(blank=True)
from .models import *
from django.contrib import admin

# Register your models here.
admin.site.register(Admin)
admin.site.register(Reader)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(BookCopy)
admin.site.register(UserCard)
admin.site.register(Borrowing)
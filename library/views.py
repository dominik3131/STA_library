from django.views.generic.edit import CreateView, UpdateView
from library.models import Admin, Author, Book, Borrowing, Genre, Publisher, Reader
from django.views.generic import ListView, DetailView
from django import forms
# TODO login required at left of inheritance 
# from django.contrib.auth.mixins import LoginRequiredMixin 
# TODO search on lists
# TODO restrict access for update and create only for admin
# TODO allow to borrow and return book for readers
# TODO allow to add book copies for admins

# ===================ADMINS===============================
class AdminListView(ListView):
    model = Admin
    
class AdminDetail(DetailView):
    model = Admin

class AdminCreateForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields= ['username', 'password', 'last_name', 'first_name', 'email' ]
        widgets = {
            'password': forms.PasswordInput()
        }

class AdminCreate(CreateView):
    form_class = AdminCreateForm
    model = Admin
    template_name_suffix = '_create_form'

    def get_success_url(self):
        return '/admins/'+str(self.object.id)+'/details'

class AdminUpdate(UpdateView):
    model = Admin
    fields= ['username', 'last_name', 'first_name', 'email' ]
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return '/readers/'+str(self.get_object().id)+'/details'
# ===================READERS===============================
class ReaderListView(ListView):
    model = Reader

class ReaderDetail(DetailView):
    model = Reader

class ReaderCreateForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields= ['username', 'password', 'last_name', 'first_name', 'email' ]
        widgets = {
            'password': forms.PasswordInput()
        }

class ReaderCreate(CreateView):
    form_class = ReaderCreateForm
    model = Reader
    template_name_suffix = '_create_form'

    def get_success_url(self):
        return '/readers/'+str(self.object.id)+'/details'

class ReaderUpdate(UpdateView):
    model = Reader
    fields= ['username', 'last_name', 'first_name', 'email' ]
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return '/readers/'+str(self.get_object().id)+'/details'

# ===================BOOKS===============================

class BookListView(ListView):
    model = Book

class BookDetail(DetailView):
    model = Book

class BookCreate(CreateView):
    fields= ['title', 'isbn', 'authors', 'genres', 'publisher' ]
    model = Book
    template_name_suffix = '_create_form'

    def get_success_url(self):
        return '/books/'+str(self.object.id)+'/details'

class BookUpdate(UpdateView):
    model = Book
    fields= ['title', 'isbn', 'authors', 'genres', 'publisher' ]
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return '/books/'+str(self.get_object().id)+'/details'


# ===================AUTHORS===============================

class AuthorListView(ListView):
    model = Author

class AuthorDetail(DetailView):
    model = Author

class AuthorCreate(CreateView):
    fields= ['first_name', 'last_name' ]
    model = Author
    template_name_suffix = '_create_form'

    def get_success_url(self):
        return '/authors/'+str(self.object.id)+'/details'

class AuthorUpdate(UpdateView):
    model = Author
    fields= ['first_name', 'last_name' ]
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return '/authors/'+str(self.get_object().id)+'/details'

# ===================PUBLISHERS===============================

class PublisherListView(ListView):
    model = Publisher

class PublisherDetail(DetailView):
    model = Publisher

class PublisherCreate(CreateView):
    fields= ['name', 'city' ]
    model = Publisher
    template_name_suffix = '_create_form'

    def get_success_url(self):
        return '/publishers/'+str(self.object.id)+'/details'

class PublisherUpdate(UpdateView):
    model = Publisher
    fields= ['name', 'city' ]
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return '/publishers/'+str(self.get_object().id)+'/details'

# ===================GENRES===============================

class GenreListView(ListView):
    model = Genre

class GenreDetail(DetailView):
    model = Genre

class GenreCreate(CreateView):
    fields= ['name']
    model = Genre
    template_name_suffix = '_create_form'

    def get_success_url(self):
        return '/genres/'+str(self.object.id)+'/details'

class GenreUpdate(UpdateView):
    model = Genre
    fields= ['name']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return '/genres/'+str(self.get_object().id)+'/details'

# ===================BORROW===============================

class BorrowingListView(ListView):
    model = Borrowing

class BorrowingDetail(DetailView):
    model = Borrowing
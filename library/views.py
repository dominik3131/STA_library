from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.db.models import query
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from library.models import Admin, Author, Book, Borrowing, Genre, Publisher, Reader
from django.views.generic import ListView, DetailView
from django import forms
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, render

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.is_staff:
            return True
        else:
            return False

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return redirect('/unauthorized')
        else:
            return redirect('/login')
# ===================ADMINS===============================


class AdminListView(LoginRequiredMixin, ListView):
    model = Admin

    def get_queryset(self):
        try:
            query = self.request.GET.get('query',)
        except KeyError:
            query = None
        if query:
            list = Admin.objects.filter(first_name__icontains=query) | Admin.objects.filter(last_name__icontains=query) | Admin.objects.filter(username__icontains=query) | Admin.objects.filter(email__icontains=query)
        else:
            list = Admin.objects.all()
        return list


class AdminDetail(LoginRequiredMixin, DetailView):
    model = Admin


class AdminCreateForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = Admin
        fields = ('username', 'first_name', 'last_name', 'email', 'password1')

    def __init__(self, *args, **kwargs):
        super(AdminCreateForm, self).__init__(*args, **kwargs)
        del self.fields['password2']


def AdminCreateRequest(request):
    form = AdminCreateForm()
    is_admin = True
    if request.method == "POST":
        form = AdminCreateForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            print(str(obj))
            obj.is_staff = is_admin
            obj.is_superuser = is_admin
            obj.save()

            return redirect('/admins/' + str(obj.id) + '/details')

    return render(request, 'admin_signup.html', {
        'form': form
    })


class AdminUpdate(AdminRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Admin
    fields = ['username', 'last_name', 'first_name', 'email']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return '/admins/'+str(self.get_object().id)+'/details'
# ===================READERS===============================


class ReaderListView(LoginRequiredMixin, ListView):
    model = Reader

    def get_queryset(self):
        try:
            query = self.request.GET.get('query',)
        except KeyError:
            query = None
        if query:
            list = Reader.objects.filter(first_name__icontains=query) | Reader.objects.filter(last_name__icontains=query) | Reader.objects.filter(username__icontains=query) | Reader.objects.filter(email__icontains=query)
        else:
            list = Reader.objects.all()
        return list

class ReaderDetail(LoginRequiredMixin, DetailView):
    model = Reader


class ReaderCreateForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = Reader
        fields = ('username', 'first_name', 'last_name', 'email', 'password1')

    def __init__(self, *args, **kwargs):
        super(ReaderCreateForm, self).__init__(*args, **kwargs)
        del self.fields['password2']


def ReaderCreateRequest(request):
    form = ReaderCreateForm()
    is_admin = True
    if request.method == "POST":
        form = ReaderCreateForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            print(str(obj))
            obj.is_staff = is_admin
            obj.is_superuser = is_admin
            obj.save()

            return redirect('/readers/' + str(obj.id) + '/details')

    return render(request, 'reader_signup.html', {
        'form': form
    })


class ReaderUpdate(AdminRequiredMixin, UpdateView):
    model = Reader
    fields = ['username', 'last_name', 'first_name', 'email']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return '/readers/'+str(self.get_object().id)+'/details'

# ===================BOOKS===============================


class BookListView(LoginRequiredMixin, ListView):
    model = Book

    def get_queryset(self):
        try:
            query = self.request.GET.get('query',)
        except KeyError:
            query = None
        if query:
            list = Book.objects.filter(title__icontains=query) | Book.objects.filter(isbn__icontains=query)
        else:
            list = Book.objects.all()
        return list

class BookDetail(LoginRequiredMixin, DetailView):
    model = Book


class BookCreate(AdminRequiredMixin, CreateView):
    fields = ['title', 'isbn', 'authors', 'genres', 'publisher']
    model = Book
    template_name_suffix = '_create_form'

    def get_success_url(self):
        return '/books/'+str(self.object.id)+'/details'


class BookUpdate(AdminRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'isbn', 'authors', 'genres', 'publisher']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return '/books/'+str(self.get_object().id)+'/details'


# ===================AUTHORS===============================

class AuthorListView(LoginRequiredMixin, ListView):
    model = Author

    def get_queryset(self):
        try:
            query = self.request.GET.get('query',)
        except KeyError:
            query = None
        if query:
            list = Author.objects.filter(first_name__icontains=query) | Author.objects.filter(last_name__icontains=query)
        else:
            list = Author.objects.all()
        return list

class AuthorDetail(LoginRequiredMixin, DetailView):
    model = Author


class AuthorCreate(AdminRequiredMixin, CreateView):
    fields = ['first_name', 'last_name']
    model = Author
    template_name_suffix = '_create_form'

    def get_success_url(self):
        return '/authors/'+str(self.object.id)+'/details'


class AuthorUpdate(AdminRequiredMixin, UpdateView):
    model = Author
    fields = ['first_name', 'last_name']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return '/authors/'+str(self.get_object().id)+'/details'

# ===================PUBLISHERS===============================


class PublisherListView(LoginRequiredMixin, ListView):
    model = Publisher

    def get_queryset(self):
        try:
            query = self.request.GET.get('query',)
        except KeyError:
            query = None
        if query:
            list = Publisher.objects.filter(name__icontains=query) | Publisher.objects.filter(city__icontains=query)
        else:
            list = Publisher.objects.all()
        return list

class PublisherDetail(LoginRequiredMixin, DetailView):
    model = Publisher


class PublisherCreate(AdminRequiredMixin, CreateView):
    fields = ['name', 'city']
    model = Publisher
    template_name_suffix = '_create_form'

    def get_success_url(self):
        return '/publishers/'+str(self.object.id)+'/details'


class PublisherUpdate(AdminRequiredMixin, UpdateView):
    model = Publisher
    fields = ['name', 'city']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return '/publishers/'+str(self.get_object().id)+'/details'

# ===================GENRES===============================


class GenreListView(LoginRequiredMixin, ListView):
    model = Genre

    def get_queryset(self):
        try:
            query = self.request.GET.get('query',)
        except KeyError:
            query = None
        if query:
            list = Genre.objects.filter(name__icontains=query)
        else:
            list = Genre.objects.all()
        return list

class GenreDetail(LoginRequiredMixin, DetailView):
    model = Genre


class GenreCreate(AdminRequiredMixin, CreateView):
    fields = ['name']
    model = Genre
    template_name_suffix = '_create_form'

    def get_success_url(self):
        return '/genres/'+str(self.object.id)+'/details'


class GenreUpdate(AdminRequiredMixin, UpdateView):
    model = Genre
    fields = ['name']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return '/genres/'+str(self.get_object().id)+'/details'

# ===================BORROW===============================


class BorrowingListView(LoginRequiredMixin, ListView):
    model = Borrowing

class BorrowingDetail(LoginRequiredMixin, DetailView):
    model = Borrowing


# ==================USER SESSION==========================
class LoginView(auth_views.LoginView):
    pass


class LogoutView(auth_views.LogoutView):
    pass


class UnauthorizedView(TemplateView):
    template_name = 'unauthorized.html'

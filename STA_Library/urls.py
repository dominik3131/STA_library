"""STA_Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from library.views import *


urlpatterns = [
    path('', BookListView.as_view()),
    path('admin/', admin.site.urls),
    path('unauthorized/', UnauthorizedView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('admins/', AdminListView.as_view()),
    path('admins/<int:pk>/details', AdminDetail.as_view()),
    path('admins/<int:pk>/update', AdminUpdate.as_view()),
    path('admins/create', AdminCreateRequest),
    path('readers/', ReaderListView.as_view()),
    path('readers/<int:pk>/details', ReaderDetail.as_view()),
    path('readers/<int:pk>/update', ReaderUpdate.as_view()),
    path('readers/create', ReaderCreateRequest),
    path('books/', BookListView.as_view()),
    path('books/<int:pk>/details', BookDetail.as_view()),
    path('books/<int:pk>/update', BookUpdate.as_view()),
    path('books/create', BookCreate.as_view()),
    path('authors/', AuthorListView.as_view()),
    path('authors/<int:pk>/details', AuthorDetail.as_view()),
    path('authors/<int:pk>/update', AuthorUpdate.as_view()),
    path('authors/create', AuthorCreate.as_view()),
    path('genres/', GenreListView.as_view()),
    path('genres/<int:pk>/details', GenreDetail.as_view()),
    path('genres/<int:pk>/update', GenreUpdate.as_view()),
    path('genres/create', GenreCreate.as_view()),
    path('publishers/', PublisherListView.as_view()),
    path('publishers/<int:pk>/details', PublisherDetail.as_view()),
    path('publishers/<int:pk>/update', PublisherUpdate.as_view()),
    path('publishers/create', PublisherCreate.as_view()),
    path('borrowings/', BorrowingListView.as_view()),
    path('borrowings/<int:pk>/details', BorrowingDetail.as_view()),
]

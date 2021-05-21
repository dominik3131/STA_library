from library.models import Admin, Reader
from django.shortcuts import render
from django.views.generic import ListView

class AdminListView(ListView):
    model = Admin
    

class ReaderListView(ListView):
    model = Reader
   
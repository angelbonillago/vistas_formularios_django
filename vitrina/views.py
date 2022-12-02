from django.shortcuts import render
# Create your views here.

from django.views.generic.list import ListView
from .models import Books

class BookList(ListView):
    model = Books
    template_name = "booklist.html" #
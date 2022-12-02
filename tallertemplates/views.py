from django.shortcuts import render

# Create your views here.

from django.views.generic.list import ListView
from .models import Libros

class BookList(ListView):
    model = Libros
    template_name = "booklist.html" #
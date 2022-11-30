from django.shortcuts import render
from django.http import HttpResponse
from .models import Laptop,Refrigeradora

# Create your views here.
def laptop(request):
    data =Laptop.objects.all().values #SELECT *FROM Laptop
    data_dict = {
        'titulo':'Listado de laptop',
        'laptops': data
    }
    return render(request,'laptop/index.html',data_dict)
    #return HttpResponse(lap)

#vista basada en funciones
def refrigeradora(request):
    data =Refrigeradora.objects.all().values #SELECT *FROM Laptop
    data_dict = {
        'titulo':'Listado de Refrigeradoras',
        'refrigeradoras': data
    }
    return render(request,'refrigeradoras/index.html',data_dict)
    return HttpResponse("hola.")

def index3(request):
    return HttpResponse("hola.")
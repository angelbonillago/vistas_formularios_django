from django.shortcuts import render
from django.http import HttpResponse
from .models import Laptop,Refrigeradora
from django.views import View
from .forms import InputForm

# Create your views here.

#vista basada en funciones
def index_view(request):

    #data =Laptop.objects.all().values #SELECT *FROM Laptop
    #data_dict = {
   #     'titulo':'Listado de laptop',
    #    'laptops': data
    #}
   # return render(request,'laptop/index.html',data_dict)
    if request.method == "GET":
        print("GET verlo mejor")
    elif request.method == "POST":
        print("POST")
        return HttpResponse("Index")

    return render(request, "index.html", {})
 
    
    #return HttpResponse(lap)

#vista basada en funciones
def refrigeradora(request):
    data =Refrigeradora.objects.all().values #SELECT *FROM Laptop
    data_dict = {
        'titulo':'Listado de Refrigeradoras',
        'refrigeradoras': data
    }

    return render(request,'refrigeradoras/index.html',data_dict)
    #return HttpResponse("hola.")

#VBF
def form_view(request):
    context = {}
    context['form']= InputForm()


    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():  #is_sumbmit-> Flask
            return HttpResponse(
                "Ingresaste el aula "
                + form.cleaned_data["aula"]
                + " y tiene la hora de entrada "
                + str(form.cleaned_data["hora_entrada"])
            )

        #registro en una BD
        

    return render(request, "form.html", context)




#vistas basada en clases
class index_view2(View):
    template='indexc.html'
    context={
            'name':'Angel',
            'lista':[1,2,3,4]
    }
    def get(self, request):
        print("GET desde una view bassada en clases")

        return render(request,self.template,self.context)

    def post(self, request):
        print("POST")
        return HttpResponse("Index Post")



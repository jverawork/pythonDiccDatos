from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import cmd_basesdatos_t

def inicio(request):
    #return HttpResponse("¡Esta es la página de inicio!")
    return render(request, "inicio.html")

def basedatos(request):
    #return HttpResponse("¡Esta es la página de bdd!")
    list_bdd = cmd_basesdatos_t.objects.all
    contexto =  {'list_bdd': list_bdd}
    contexto['usuario']= request.user.username
    return render(request, "basedatos.html", contexto)

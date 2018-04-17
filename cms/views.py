from django.shortcuts import render
from django.http import HttpResponse
from .models import Pages

# Create your views here.

def buscar(peticion,identificador):
	try:
		pagina = Pages.objects.get(name = identificador)
		respuesta = pagina.page
	except Pages.DoesNotExist:
		respuesta = "No hay datos en la base de datos"
	return HttpResponse(respuesta)

def informacion(peticion):
	respuesta = "Lista de páginas:  <br/>"
	lista = Pages.objects.all()
	for pag in lista:
		respuesta += "</ol>" + str(pag.id)+ '. ' + str(pag.page) + ' es la página de '  + pag.name  + "<br/>"
	respuesta += "</ol>"
	return HttpResponse(respuesta)

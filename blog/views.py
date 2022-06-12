from django.http import HttpResponse
from django.shortcuts import render

def saludo(request, nombre):
	return HttpResponse(f'Hola Django - Coder {nombre}')

def probando_template(request):
	return render(request, 'index.html', context = {})
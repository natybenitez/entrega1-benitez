from django.http import HttpResponse

def saludo(request, nombre):
	return HttpResponse(f'Hola Django - Coder {nombre}')

    
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render
from models import Contacto

# Create your views here.

def home(request):
	return render(request, 'index.html')

def noticia(request):
	return render(request, 'noticia_detalle.html')

def contacto(request):
	contactos = Contacto.objects.all()
	return render(request, 'contacto.html', {'contactos': contactos})

def contacto_detalle(request,contacto_id):
	try:
		detalle = Contacto.objects.get(id=contacto_id)
		direccion = detalle.direccion
		direccion_plus = direccion.replace(" ", "+")
		return render(request, 'contacto_detalle.html', {'contacto': detalle, 'direccion': direccion_plus})
	except ObjectDoesNotExist:
		raise Http404()
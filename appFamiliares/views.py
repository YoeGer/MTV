from django.shortcuts import render
from .models import Familiares 
from django.http import HttpResponse 


def familiares(request):
    familiar1 = Familiares(nombre = 'Julian', edad = 38, cumpleanios = '1986-07-02' )
    familiar2 = Familiares(nombre = 'Ernesto', edad = 62, cumpleanios = '1960-10-21')
    familiar3 = Familiares(nombre = 'Maria Luisa', edad = 58, cumpleanios = '1964-06-04')
    familiar1.save()
    familiar2.save()
    familiar3.save()
    texto= f'Los familiares creados son: --- HERMANO: {familiar1.nombre} --- PAPA: {familiar2.nombre} --- MAMA: {familiar3.nombre}'
    return HttpResponse(texto)
    
    

def inicio(request): 
    return render (request, "appFamiliares/inicio.html")
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
    texto1 = f'HERMANO: {familiar1.nombre}, de {familiar1.edad} anios y fecha de nacimiento {familiar1.cumpleanios}'
    texto2 = f'PAPA: {familiar2.nombre}, de {familiar2.edad} anios y fecha de nacimiento {familiar2.cumpleanios}'
    texto3 = f'MAMA: {familiar3.nombre}, de {familiar3.edad} anios y fecha de nacimiento {familiar3.cumpleanios}'
    return HttpResponse(texto1, texto2, texto3)
    

def inicio(request): 
    return render (request, 'appFamiliares/inicio.html')
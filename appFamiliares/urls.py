from appFamiliares.views import *
from django.urls import path

urlpatterns = [
    path('inicio/', inicio),
    path('familiares/', familiares),
    
]
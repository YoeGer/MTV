from appFamiliares.views import *
from django.urls import path

urlpatterns = [
    path('familiares/', familiares, name='familiares'),
    path('inicio/', inicio),
]
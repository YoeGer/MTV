from django.db import models

class Familiares(models.Model): 
    nombre = models.CharField(max_length = 50)
    edad = models.IntegerField()
    cumpleanios = models.DateField() 
    
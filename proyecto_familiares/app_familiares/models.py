from django.db import models

class Familiar (models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()

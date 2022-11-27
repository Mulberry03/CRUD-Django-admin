from collections import UserString
from django.db import models

# Create your models here.
class Trabajadores(models.Model):
    Rut = models.CharField(max_length=12)
    Nombre = models.CharField(max_length=30)
    Email = models.EmailField(max_length=50)
    Telefono = models.CharField(max_length=12)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True)
    important = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'trabajadores'


    def __str__(self):
        return self.Nombre

    
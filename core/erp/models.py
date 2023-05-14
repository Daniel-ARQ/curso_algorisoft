from django.db import models
from datetime import datetime

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')

    def __str__(self):
      return self.name
    class Meta:
      verbose_name = 'Tipo'
      verbose_name_plural = 'Tipos'
      ordering = ['id']


class category(models.Model):
   name = models.CharField(max_length=50, verbose_name='Nombre')

   def __str__(self):
      return self.name
   class Meta:
      verbose_name = 'categoria'
      verbose_name_plural = 'categorias'
      ordering = ['id']



class Employee(models.Model):
    #de esta manera relacionamos las tablas con la utilizacion de la llave foranea
    categ = models.ManyToManyField(category)
    type = models.ForeignKey(Type,on_delete = models.CASCADE)
    name = models.CharField(max_length=150, verbose_name='Nombre')
    cedula = models.IntegerField( unique=True,verbose_name='Cedula')
    fechaNaci = models.DateField(default=datetime.now, verbose_name='Fecha Nacimiento')
    fechaRegis = models.DateTimeField(auto_now=True,)

    def __str__(self):
      return self.name 

    class Meta:
      verbose_name = 'Empleado'
      verbose_name_plural = 'Empleados'
      db_table = 'empleado'
      ordering = ['id'] 

#ORM  es el mapeo de objetos relacionados,en donde podemos interactuar con muchas cosas de las base de datos.

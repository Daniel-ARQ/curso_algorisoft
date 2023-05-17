from django.db import models
from datetime import datetime

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre', unique=True)

    def __str__(self):
      return self.name
    class Meta:
      verbose_name = 'Tipo'
      verbose_name_plural = 'Tipos'
      ordering = ['id'] 
      db_table = 'tipo'


class category(models.Model):
   name = models.CharField(max_length=50, verbose_name='Nombre')

   def __str__(self):
      return self.name
   class Meta:
      verbose_name = 'categoria'
      verbose_name_plural = 'categorias'
      ordering = ['id']
      db_table = 'categora'



class Employee(models.Model):
    #de esta manera relacionamos las tablas con la utilizacion de la llave foranea
    categ = models.ManyToManyField(category)
    type = models.ForeignKey(Type,on_delete = models.CASCADE)
    name = models.CharField(max_length=150, verbose_name='Nombre')
    cedula = models.IntegerField( unique=True,verbose_name='Cedula')
    fechaNaci = models.DateField(default=datetime.now, verbose_name='Fecha Nacimiento')
    fechaRegis = models.DateTimeField(auto_now=True,)
    edad = models.PositiveIntegerField(default='0')
    salario = models.DecimalField(default='0.00',max_digits='9',decimal_places='2')
    estado = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
    corri = models.FileField(upload_to='corri/%Y/%m/%d', null=True, blank=True)



    def __str__(self):
      return self.name 

    class Meta:
      verbose_name = 'Empleado'
      verbose_name_plural = 'Empleados'
      db_table = 'empleado'
      ordering = ['id'] 

#ORM  es el mapeo de objetos relacionados,en donde podemos interactuar con muchas cosas de las base de datos.

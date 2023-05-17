from dotenv import load_dotenv
load_dotenv('./.env')
from config.wsgi import *


from core.erp.models import *
# listar
#query = Type.objects.all()
#print(query)

#LISTAR MEDIANTE FILTER(FILTRAR)
n = Type.objects.filter(name__icontains=('pre'))
print(n)


#Insercion// puede hacerse de manera simplificada o extendida como se muestra a acontinuacion
#SIMPLIFICADO
#n= Type(name='Socio').save()

#EXTENDIDO
#n = Type()
#n.name = 'Gerente'
#n.save()

#TOMAR DATOS EXPESIFICOS
#n = Type.objects.get(id=4)
#print(n.name)

#EDITAR
#n = Type.objects.get(id=3)
#n.name = 'Secretaria'
#n.save()

#ELIMINAR
#n = Type.objects.get(id=5)
#n.delete()



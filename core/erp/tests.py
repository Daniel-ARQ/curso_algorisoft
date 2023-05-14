import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.erp.models import *

# listar
query = Type.objects.all()
print(query)



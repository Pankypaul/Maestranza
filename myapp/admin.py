from django.contrib import admin
from .models import Producto, Categoria, Marca, Proveedor, Productos


admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Proveedor)
admin.site.register(Productos)
from django.contrib import admin
from .models import Usuario, Cliente, Ordene, Servicio, Producto, Detalleorde

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Ordene)
admin.site.register(Servicio)
admin.site.register(Producto)
admin.site.register(Detalleorde)

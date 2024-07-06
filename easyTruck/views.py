from django.shortcuts import render
from .models import Usuario, Cliente, Ordene, Servicio, Producto, Detalleorder


# Create your views here.
def index(resquest):
    return render(resquest, 'index.html')

def nosotros(resquest):
    return render(resquest, 'nosotros.html')

def servicios(resquest):
    return render(resquest, 'servicios.html')

def productos(resquest):
    return render(resquest, 'productos.html')

def clientes(resquest):
    return render(resquest, 'clientes.html')

def contacto(resquest):
    return render(resquest, 'contacto.html')
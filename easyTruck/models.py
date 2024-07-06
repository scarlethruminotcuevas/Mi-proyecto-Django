from django.db import models

# Create your models here.

class Usuario(models.Model):

    usuarioid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    passwordhash = models.CharField(max_length=50)
    fechacreacion = models.DateTimeField(auto_now_add=True)
    tipousuario = models.CharField(max_length=50)

    def __str__(self) :
        return str(self.usuarioid) + " " + str(self.nombre) + " " + str(self.apellido) + " " + str(self.email) + " " + str(self.passwordhash) + " " + str(self.fechacreacion) + " " + str(self.tipousuario)

class Cliente(models.Model):
    
    clienteid = models.AutoField(primary_key=True)
    usuarioid = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='usuarioid')
    empresa = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)

    def __str__(self) :
        return str(self.clienteid) + " " + str(self.usuarioid) + " " + str(self.empresa) + " " + str(self.direccion) + " " + str(self.telefono)
    

class Ordene(models.Model):
    
    ordenid = models.AutoField(primary_key=True)
    clienteid = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='clienteid')
    fechaorden = models.DateTimeField(auto_now_add=True)
    total = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)

    def __str__(self) :
        return str(self.ordenid) + " " + str(self.clienteid) + " " + str(self.fechaorden) + " " + str(self.total) + " " + str(self.estado)

class Servicio(models.Model):
    
    servicioid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.CharField(max_length=50)
    fechacreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return str(self.servicioid) + " " + str(self.nombre) + " " + str(self.descripcion) + " " + str(self.precio) + " " + str(self.fechacreacion)


class Producto(models.Model):
    
    productoid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.CharField(max_length=50)
    stock = models.CharField(max_length=50)
    fechacreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return str(self.productoid) + " " + str(self.nombre) + " " + str(self.descripcion) + " " + str(self.precio) + " " + str(self.stock) + " " + str(self.fechacreacion)
    
class Detalleorde(models.Model):
    
    detalleid = models.AutoField(primary_key=True)
    ordenid = models.ForeignKey(Ordene, on_delete=models.CASCADE, db_column='ordenid')
    productoid = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='productoid')
    servicioid = models.ForeignKey(Servicio, on_delete=models.CASCADE, db_column='servicioid')
    cantidad = models.CharField(max_length=50)
    preciounitario = models.CharField(max_length=50)

    def __str__(self) :
        return str(self.detalleid) + " " + str(self.ordenid) + " " + str(self.productoid) + " " + str(self.servicioid) + " " + str(self.cantidad) + " " + str(self.preciounitario)
    

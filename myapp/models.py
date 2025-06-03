from django.db import models

class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=50)


    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    TIPO_USUARIO = [
        (0, 'Administrador'),
        (1, 'Gestor de Inventario'),
        (2, 'Comprador'),
        (3, 'Encargado de Logística'),
        (4, 'Jefe de Producción'),
        (5, 'Auditor de Inventario'),
        (6, 'Gerente de Proyectos'),
        (7, 'Trabajador de Planta'),
    ]

    nombre = models.CharField(max_length=100)
    telefono = models.IntegerField()
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=50)
    tipo_id = models.IntegerField(choices=TIPO_USUARIO, default=7)

    def __str__(self):
        return self.nombre



class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField() 

    stock = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, null=True, blank=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} (ID: {self.id})"
    
    def imagen_url(self):
        return f'/media/productos/{self.imagen}'
    
    def __str__(self):
        return self.nombre

class OrdenCompra(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    productos = models.ManyToManyField(Producto)
    cantidad = models.IntegerField(default=0)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Orden #{self.id} de {self.usuario.nombre}"
    

class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField() 
    stock = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, null=True, blank=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} (ID: {self.id})"
    
    def imagen_url(self):
        return f'/media/productos/{self.imagen}'
    
    def __str__(self):
        return self.nombre
    
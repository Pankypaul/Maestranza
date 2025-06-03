from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from myapp.models import Producto, HistorialPrecio
from random import randint, choice

class Command(BaseCommand):
    help = 'Carga datos de demostración'

    def handle(self, *args, **options):
        # 1. Manejo de usuarios existentes
        usuarios_data = [
            {'username': 'comprador1', 'password': 'demo123', 'is_staff': False},
            {'username': 'comprador2', 'password': 'demo123', 'is_staff': False},
            {'username': 'admin', 'password': 'admin123', 'is_staff': True}
        ]
        
        usuarios = []
        for user_data in usuarios_data:
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                defaults={
                    'is_staff': user_data['is_staff']
                }
            )
            if created:
                user.set_password(user_data['password'])
                user.save()
            usuarios.append(user)
            status = "Creado" if created else "Recuperado"
            self.stdout.write(f"Usuario {user.username}: {status}")

        # 2. Limpiar datos de demostración anteriores (opcional)
        Producto.objects.all().delete()
        self.stdout.write("Datos antiguos de demostración eliminados")

        # 3. Crear productos
        nombres_productos = ["Tornillo", "Tuerca", "Arandela", "Clavo", "Martillo"]
        productos = []
        
        for nombre in nombres_productos:
            p = Producto.objects.create(
                nombre=nombre,
                descripcion=f"Descripción de {nombre}",
                precio=randint(100, 1000),
                stock=randint(10, 100),
                imagen='productos/default.png'  # Asegúrate de tener esta imagen
            )
            productos.append(p)
            
            # Crear historial de precios
            for _ in range(3):
                HistorialPrecio.objects.create(
                    producto=p,
                    precio=p.precio - randint(50, 150),
                )

        self.stdout.write(self.style.SUCCESS('¡Datos de demostración creados exitosamente!'))
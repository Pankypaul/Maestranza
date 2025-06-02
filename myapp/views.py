from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .models import Producto , Categoria, Marca, Proveedor
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProveedorForm
from .forms import MarcaForm
from .forms import CategoriaForm
from .forms import ProductoForm
from .forms import EditarProductoForm
from .models import Usuario
from .forms import LoginForm
from .forms import UsuarioForm
from .forms import EditarUsuarioForm

def index(request):
    return render(request, 'index.html')

def crear_productos_iniciales():
    productos_iniciales = [
        {'nombre': "Martillo de Acero", 'descripcion': "Martillo profesional con mango de fibra de vidrio",'precio': 12500,'imagen': "martillo.png", 'stock': 50},
        {'nombre': "Destornillador Phillips", 'descripcion': "Juego de destornilladores anti-deslizantes", 'precio': 8500,'imagen': "martillo.png", 'stock': 120},
        {'nombre': "Taladro Percutor 750W", 'descripcion': "Taladro con percusión y velocidad variable", 'precio': 45900,'imagen': "martillo.png", 'stock': 15},
        {'nombre': "Sierra Circular 1800W", 'descripcion': "Sierra circular profesional con láser guía", 'precio': 78900,'imagen': "martillo.png", 'stock': 8},
        {'nombre': "Llave Inglesa Ajustable", 'descripcion': "Llave de 8 a 32 mm con cabeza giratoria", 'precio': 15600,'imagen': "martillo.png", 'stock': 45},
        {'nombre': "Cemento Gris 25kg", 'descripcion': "Cemento de fraguado normal para construcción", 'precio': 8500,'imagen': "martillo.png", 'stock': 200},
        {'nombre': "Ladrillo Fiscal 6 huecos", 'descripcion': "Ladrillo cerámico estándar 6 huecos", 'precio': 350,'imagen': "martillo.png", 'stock': 1000},
        {'nombre': "Pintura Latex 4L", 'descripcion': "Pintura blanca lavable interior/exterior", 'precio': 22900,'imagen': "martillo.png", 'stock': 30},
        {'nombre': "Cerámica 45x45 cm", 'descripcion': "Piso cerámico antideslizante", 'precio': 8990,'imagen': "martillo.png", 'stock': 150},
        {'nombre': "Tubo PVC 1/2\" x 3m", 'descripcion': "Tubería para instalaciones sanitarias", 'precio': 3200,'imagen': "martillo.png", 'stock': 80},
        {'nombre': "Cable Eléctrico 2.5mm", 'descripcion': "Cobre flexible para instalaciones", 'precio': 4500,'imagen': "martillo.png", 'stock': 120},
        {'nombre': "Interruptor Simple", 'descripcion': "Interruptor de pared para 10A", 'precio': 2500,'imagen': "martillo.png", 'stock': 60},
        {'nombre': "Lijadora Orbital", 'descripcion': "Lijadora profesional 250W con bolsa colectora", 'precio': 38900,'imagen': "martillo.png", 'stock': 12},
        {'nombre': "Nivel Laser", 'descripcion': "Nivel láser autónivelante 360°", 'precio': 65900,'imagen': "NivelLaser360.jpg", 'stock': 5},
        {'nombre': "Andamio Modular", 'descripcion': "Estructura metálica para trabajo en altura", 'precio': 125000,'imagen': "andamio.jpg", 'stock': 3},
        {'nombre': "Carretilla de Obra", 'descripcion': "Carretilla metálica 6 pies cúbicos", 'precio': 45900,'imagen': "martillo.png", 'stock': 18},
        {'nombre': "Mezcladora de Pintura", 'descripcion': "Accesorio para taladro para mezclar pintura", 'precio': 8900,'imagen': "martillo.png", 'stock': 25},
        {'nombre': "Broca para Concreto 1/2\"", 'descripcion': "Juego de brocas widia para concreto", 'precio': 12900,'imagen': "martillo.png", 'stock': 40},
        {'nombre': "Guantes de Seguridad", 'descripcion': "Guantes anticorte nivel 5", 'precio': 9900,'imagen': "martillo.png", 'stock': 75},
        {'nombre': "Casco de Seguridad", 'descripcion': "Casco con ajuste ergonómico y visera", 'precio': 7500,'imagen': "martillo.png", 'stock': 50}
    ]
    
    for prod in productos_iniciales:
        if not Producto.objects.filter(nombre=prod['nombre']).exists():
            Producto.objects.create(**prod)

#ESTE FUNCIONA PERO LO DEJARE COMENTADO
"""
def catalogo(request):
    crear_productos_iniciales()

    productos = Producto.objects.all()
    nombre = request.GET.get('nombre', '')
    categoria_id = request.GET.get('categoria', '')
    orden = request.GET.get('orden', 'id')  # por defecto 'id'

    if nombre:
        productos = productos.filter(nombre__icontains=nombre)
    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)

    # Validar orden
    opciones_validas = ['id', '-id', 'nombre', '-nombre', 'precio', '-precio']
    if orden in opciones_validas:
        productos = productos.order_by(orden)
    else:
        productos = productos.order_by('nombre')

    usuario = None
    if 'usuario_id' in request.session:
        try:
            usuario = Usuario.objects.get(id=request.session['usuario_id'])
        except Usuario.DoesNotExist:
            usuario = None

    categorias = Categoria.objects.all()

    return render(request, 'catalogo.html', {
        'productos': productos,
        'usuario': usuario,
        'categorias': categorias,
        'filtro_nombre': nombre,
        'filtro_categoria': categoria_id,
        'filtro_orden': orden,
    })

"""

from django.shortcuts import render
from .models import Producto, Categoria, Marca, Proveedor

def catalogo(request):
    # Obtener parámetros GET
    orden = request.GET.get('orden', 'id')  # Orden por defecto 'id'
    categoria_id = request.GET.get('categoria', '')  # Puede ser '' o 'none' o id
    marca_id = request.GET.get('marca', '')
    proveedor_id = request.GET.get('proveedor', '')

    productos = Producto.objects.all()

    # Filtrar categoría
    if categoria_id and categoria_id != '' and categoria_id != 'all':
        if categoria_id == 'none':
            productos = productos.filter(categoria__isnull=True)
        else:
            productos = productos.filter(categoria__id=categoria_id)

    # Filtrar marca
    if marca_id and marca_id != '' and marca_id != 'all':
        if marca_id == 'none':
            productos = productos.filter(marca__isnull=True)
        else:
            productos = productos.filter(marca__id=marca_id)

    # Filtrar proveedor
    if proveedor_id and proveedor_id != '' and proveedor_id != 'all':
        if proveedor_id == 'none':
            productos = productos.filter(proveedor__isnull=True)
        else:
            productos = productos.filter(proveedor__id=proveedor_id)

    # Ordenar
    productos = productos.order_by(orden)

    # Para llenar los selects
    categorias = Categoria.objects.all()
    marcas = Marca.objects.all()
    proveedores = Proveedor.objects.all()

    return render(request, 'catalogo.html', {
        'productos': productos,
        'categorias': categorias,
        'marcas': marcas,
        'proveedores': proveedores,
        'orden_seleccionado': orden,
        'categoria_seleccionada': categoria_id,
        'marca_seleccionada': marca_id,
        'proveedor_seleccionado': proveedor_id,
    })

#------------------------------------------------------------------------------------------------------------

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'detalle_producto.html', {'producto': producto})



def admin_panel(request):
    return render(request, 'admin-panel.html', {
        'productos': Producto.objects.all(),
        'usuarios': Usuario.objects.all()  
    })
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})





def agregarProducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('catalogo')  
        else:
            print(form.errors) 
    else:
        form = ProductoForm()
    
    return render(request, 'agregarProducto.html', {'form': form})



def agregarCategoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogo')  
    else:
        form = CategoriaForm()

    return render(request, 'agregarCategoria.html', {'form': form})




def agregarMarca(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogo')  
    else:
        form = MarcaForm()

    return render(request, 'agregarMarca.html', {'form': form})





def agregarProveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogo')  
    else:
        form = ProveedorForm()

    return render(request, 'agregarProveedor.html', {'form': form})



def editarProducto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        form = EditarProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('catalogo')  
    else:
        form = EditarProductoForm(instance=producto)

    return render(request, 'editarProducto.html', {'form': form, 'producto': producto})


def eliminarProducto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        producto.delete()
        return redirect('catalogo')  

    return render(request, 'eliminarProducto.html', {'producto': producto})


def registro(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = UsuarioForm()
    return render(request, 'registro.html', {'form': form})


def login_view(request):
    error = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['correo']
            contrasena = form.cleaned_data['contrasena']
            try:
                usuario = Usuario.objects.get(correo=correo, contrasena=contrasena)
                request.session['usuario_id'] = usuario.id 

                
                if usuario.tipo_id == 0: 
                    return redirect('admin_panel')
                else:
                    return redirect('catalogo')

            except Usuario.DoesNotExist:
                error = "Correo o contraseña incorrectos"
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form, 'error': error})


def home(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('login')
    
def logout_view(request):
    request.session.flush()
    return redirect('login')

def eliminarUsuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)

    if request.method == 'POST':
        usuario.delete()
        return redirect('admin_panel')  

    return render(request, 'eliminarUsuario.html', {'usuario': usuario})


def editarUsuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)

    if request.method == 'POST':
        form = EditarUsuarioForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')  
    else:
        form = EditarUsuarioForm(instance=usuario)

    return render(request, 'editarUsuario.html', {'form': form, 'usuario': usuario})

from .models import Proveedor  # Asegúrate de importar el modelo

def proveedores_view(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor.html', {
        'proveedores': proveedores
    })

def editar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)

    if request.method == 'POST':
        proveedor.nombre = request.POST.get('nombre')
        proveedor.correo = request.POST.get('correo')
        proveedor.telefono = request.POST.get('telefono')
        proveedor.direccion = request.POST.get('direccion')
        proveedor.save()
        return redirect('proveedor')

    return render(request, 'editar_proveedor.html', {'proveedor': proveedor})


#-----------------------------------------------

def eliminar_proveedor(request, id):  # Aquí debe coincidir el nombre con el de la URL
    proveedor = get_object_or_404(Proveedor, id=id)

    if request.method == 'POST':
        proveedor.delete()
        return redirect('proveedor')  # Asegúrate de que esta URL esté definida con ese name

    return render(request, 'eliminar_proveedor.html', {'proveedor': proveedor})

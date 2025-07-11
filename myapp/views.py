from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .models import Carrito, HistorialPrecio, Producto , Categoria, Marca, Proveedor
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import redirect
from .forms import ProveedorForm
from .forms import MarcaForm
from .forms import CategoriaForm
from .forms import ProductoForm
from .forms import EditarProductoForm
from .models import Usuario
from .forms import LoginForm
from .forms import UsuarioForm
from .forms import EditarUsuarioForm
from .models import Productos
from datetime import date
from .models import OrdenCompra, ProductoOrdenado


def index(request):
    return render(request, 'index.html')

def crear_productos_iniciales():
    productos_iniciales = [
        {'nombre': "Martillo de Acero", 'descripcion': "Martillo profesional con mango de fibra de vidrio",'imagen': "martillo.png", 'stock': 50},
        {'nombre': "Destornillador Phillips", 'descripcion': "Juego de destornilladores anti-deslizantes",'imagen': "martillo.png", 'stock': 120},
        {'nombre': "Taladro Percutor 750W", 'descripcion': "Taladro con percusión y velocidad variable",'imagen': "martillo.png", 'stock': 15},
        {'nombre': "Sierra Circular 1800W", 'descripcion': "Sierra circular profesional con láser guía",'imagen': "martillo.png", 'stock': 8},
        {'nombre': "Llave Inglesa Ajustable", 'descripcion': "Llave de 8 a 32 mm con cabeza giratoria",'imagen': "martillo.png", 'stock': 45},
        {'nombre': "Cemento Gris 25kg", 'descripcion': "Cemento de fraguado normal para construcción",'imagen': "martillo.png", 'stock': 200},
        {'nombre': "Ladrillo Fiscal 6 huecos", 'descripcion': "Ladrillo cerámico estándar 6 huecos",'imagen': "martillo.png", 'stock': 1000},
        {'nombre': "Pintura Latex 4L", 'descripcion': "Pintura blanca lavable interior/exterior",'imagen': "martillo.png", 'stock': 30},
        {'nombre': "Cerámica 45x45 cm", 'descripcion': "Piso cerámico antideslizante",'imagen': "martillo.png", 'stock': 150},
        {'nombre': "Tubo PVC 1/2\" x 3m", 'descripcion': "Tubería para instalaciones sanitarias",'imagen': "martillo.png", 'stock': 80},
        {'nombre': "Cable Eléctrico 2.5mm", 'descripcion': "Cobre flexible para instalaciones",'imagen': "martillo.png", 'stock': 120},
        {'nombre': "Interruptor Simple", 'descripcion': "Interruptor de pared para 10A",'imagen': "martillo.png", 'stock': 60},
        {'nombre': "Lijadora Orbital", 'descripcion': "Lijadora profesional 250W con bolsa colectora",'imagen': "martillo.png", 'stock': 12},
        {'nombre': "Nivel Laser", 'descripcion': "Nivel láser autónivelante 360°",'imagen': "NivelLaser360.jpg", 'stock': 5},
        {'nombre': "Andamio Modular", 'descripcion': "Estructura metálica para trabajo en altura",'imagen': "andamio.jpg", 'stock': 3},
        {'nombre': "Carretilla de Obra", 'descripcion': "Carretilla metálica 6 pies cúbicos",'imagen': "martillo.png", 'stock': 18},
        {'nombre': "Mezcladora de Pintura", 'descripcion': "Accesorio para taladro para mezclar pintura",'imagen': "martillo.png", 'stock': 25},
        {'nombre': "Broca para Concreto 1/2\"", 'descripcion': "Juego de brocas widia para concreto",'imagen': "martillo.png", 'stock': 40},
        {'nombre': "Guantes de Seguridad", 'descripcion': "Guantes anticorte nivel 5",'imagen': "martillo.png", 'stock': 75},
        {'nombre': "Casco de Seguridad", 'descripcion': "Casco con ajuste ergonómico y visera",'imagen': "martillo.png", 'stock': 50}
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

    usuario = None

    if 'usuario_id' in request.session:
        try:
            usuario = Usuario.objects.get(id=request.session['usuario_id'])
        except Usuario.DoesNotExist:
            usuario = None

    return render(request, 'catalogo.html', {
        'productos': productos,
        'categorias': categorias,
        'marcas': marcas,
        'proveedores': proveedores,
        'orden_seleccionado': orden,
        'categoria_seleccionada': categoria_id,
        'marca_seleccionada': marca_id,
        'proveedor_seleccionado': proveedor_id,
        'usuario': usuario,             
    })


#------------------------------------------------------------------------------------------------------------

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    usuario = None

    if 'usuario_id' in request.session:
        try:
            usuario = Usuario.objects.get(id=request.session['usuario_id'])
        except Usuario.DoesNotExist:
            usuario = None
    return render(request, 'detalle_producto.html', {
        'producto': producto,
        'usuario': usuario, 
        })

def detalle_productos(request, producto_id):
    producto = get_object_or_404(Productos, id=producto_id)
    usuario = None

    if 'usuario_id' in request.session:
        try:
            usuario = Usuario.objects.get(id=request.session['usuario_id'])
        except Usuario.DoesNotExist:
            usuario = None
    return render(request, 'detalle_productos.html', {
        'producto': producto,
        'usuario': usuario, 
        })




def admin_panel(request):
    usuario = None

    if 'usuario_id' in request.session:
        try:
            usuario = Usuario.objects.get(id=request.session['usuario_id'])
        except Usuario.DoesNotExist:
            usuario = None
    return render(request, 'admin-panel.html', {
        'productos': Producto.objects.all(),
        'usuarios': Usuario.objects.all(),
        'usuario': usuario,  
    })

def registro(request):
    usuario = None

    if 'usuario_id' in request.session:
        try:
            usuario = Usuario.objects.get(id=request.session['usuario_id'])
        except Usuario.DoesNotExist:
            usuario = None
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {
        'form': form,
        'usuario': usuario, 
        })





def agregarProducto(request):
    usuario = None

    if 'usuario_id' in request.session:
        try:
            usuario = Usuario.objects.get(id=request.session['usuario_id'])
        except Usuario.DoesNotExist:
            usuario = None
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('catalogo')  
        else:
            print(form.errors) 
    else:
        form = ProductoForm()
    
    return render(request, 'agregarProducto.html', {
        'form': form,
        'usuario': usuario, 
        })



def agregarCategoria(request):
    usuario = None

    if 'usuario_id' in request.session:
        try:
            usuario = Usuario.objects.get(id=request.session['usuario_id'])
        except Usuario.DoesNotExist:
            usuario = None
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogo')  
    else:
        form = CategoriaForm()

    return render(request, 'agregarCategoria.html', {
        'form': form,
        'usuario': usuario,
        })




def agregarMarca(request):
    usuario = None

    if 'usuario_id' in request.session:
        try:
            usuario = Usuario.objects.get(id=request.session['usuario_id'])
        except Usuario.DoesNotExist:
            usuario = None
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogo')  
    else:
        form = MarcaForm()

    return render(request, 'agregarMarca.html', {
        'form': form,
        'usuario': usuario,
        })





def agregarProveedor(request):
    usuario = None

    if 'usuario_id' in request.session:
        try:
            usuario = Usuario.objects.get(id=request.session['usuario_id'])
        except Usuario.DoesNotExist:
            usuario = None
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogo')  
    else:
        form = ProveedorForm()

    return render(request, 'agregarProveedor.html', {
        'form': form,
        'usuario': usuario,
        })



def editarProducto(request, producto_id):
    usuario = None

    if 'usuario_id' in request.session:
        try:
            usuario = Usuario.objects.get(id=request.session['usuario_id'])
        except Usuario.DoesNotExist:
            usuario = None
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        form = EditarProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('catalogo')  
    else:
        form = EditarProductoForm(instance=producto)

    return render(request, 'editarProducto.html', {
        'form': form, 'producto': producto,
        'usuario': usuario,})


def eliminarProducto(request, producto_id):
    usuario = None

    if 'usuario_id' in request.session:
        try:
            usuario = Usuario.objects.get(id=request.session['usuario_id'])
        except Usuario.DoesNotExist:
            usuario = None
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        producto.delete()
        return redirect('catalogo')  

    return render(request, 'eliminarProducto.html', {
        'producto': producto,
        'usuario': usuario,
        })


def registro(request):
    usuario = None

    if 'usuario_id' in request.session:
        try:
            usuario = Usuario.objects.get(id=request.session['usuario_id'])
        except Usuario.DoesNotExist:
            usuario = None
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_panel') 
    else:
        form = UsuarioForm()
    return render(request, 'registro.html', {
        'form': form,
        'usuario': usuario,})


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
                elif usuario.tipo_id == -1:
                    return redirect('login')
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
    usuario = None

    if 'usuario_id' in request.session:
        try:
            usuario = Usuario.objects.get(id=request.session['usuario_id'])
        except Usuario.DoesNotExist:
            usuario = None
    usuarios = get_object_or_404(Usuario, id=usuario_id)

    if request.method == 'POST':
        usuarios.delete()
        return redirect('admin_panel')  

    return render(request, 'eliminarUsuario.html', {
        'usuarios': usuarios,
        'usuario': usuario,})


def editarUsuario(request, usuario_id):
    usuario = None

    if 'usuario_id' in request.session:
        try:
            usuario = Usuario.objects.get(id=request.session['usuario_id'])
        except Usuario.DoesNotExist:
            usuario = None
    usuarios = get_object_or_404(Usuario, id=usuario_id)

    if request.method == 'POST':
        form = EditarUsuarioForm(request.POST, request.FILES, instance=usuarios)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')  
    else:
        form = EditarUsuarioForm(instance=usuarios)

    return render(request, 'editarUsuario.html', {
        'form': form, 
        'usuarios': usuarios,
        'usuario': usuario,
        })



def proveedores_view(request):
    usuario = None

    if 'usuario_id' in request.session:
        try:
            usuario = Usuario.objects.get(id=request.session['usuario_id'])
        except Usuario.DoesNotExist:
            usuario = None
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor.html', {
        'proveedores': proveedores,
        'usuario': usuario,
    })

def editar_proveedor(request, id):
    usuario = None

    if 'usuario_id' in request.session:
        try:
            usuario = Usuario.objects.get(id=request.session['usuario_id'])
        except Usuario.DoesNotExist:
            usuario = None
    proveedor = get_object_or_404(Proveedor, id=id)

    if request.method == 'POST':
        proveedor.nombre = request.POST.get('nombre')
        proveedor.correo = request.POST.get('correo')
        proveedor.telefono = request.POST.get('telefono')
        proveedor.direccion = request.POST.get('direccion')
        proveedor.save()
        return redirect('proveedor')

    return render(request, 'editar_proveedor.html', {
        'proveedor': proveedor,
        'usuario': usuario,})


#-----------------------------------------------

def eliminar_proveedor(request, id):  
    usuario = None

    if 'usuario_id' in request.session:
        try:
            usuario = Usuario.objects.get(id=request.session['usuario_id'])
        except Usuario.DoesNotExist:
            usuario = None
    proveedor = get_object_or_404(Proveedor, id=id)

    if request.method == 'POST':
        proveedor.delete()
        return redirect('proveedor')  

    return render(request, 'eliminar_proveedor.html', {
        'proveedor': proveedor,
        'usuario': usuario,})


#Productos predefinidos
def crear_productos_iniciales2():
    productos_iniciales2 = [
        {'nombre': "Martillo de Acero2", 'descripcion': "Martillo profesional con mango de fibra de vidrio",'precio': 12500,'imagen': "martillo.png", 'stock': 50,'categoria': 1, 'marca': 1, 'proveedor': 1},
        {'nombre': "Destornillador Phillips2", 'descripcion': "Juego de destornilladores anti-deslizantes", 'precio': 8500,'imagen': "martillo.png", 'stock': 120,'categoria': 1, 'marca': 1, 'proveedor': 1},
        {'nombre': "Taladro Percutor 750W2", 'descripcion': "Taladro con percusión y velocidad variable", 'precio': 45900,'imagen': "martillo.png", 'stock': 15,'categoria': 1, 'marca': 1, 'proveedor': 1},
        {'nombre': "Sierra Circular 1800W2", 'descripcion': "Sierra circular profesional con láser guía", 'precio': 78900,'imagen': "martillo.png", 'stock': 8,'categoria': 1, 'marca': 1, 'proveedor': 1},
        {'nombre': "Llave Inglesa Ajustable2", 'descripcion': "Llave de 8 a 32 mm con cabeza giratoria", 'precio': 15600,'imagen': "martillo.png", 'stock': 45,'categoria': 1, 'marca': 1, 'proveedor': 1},
        {'nombre': "Cemento Gris 25kg2", 'descripcion': "Cemento de fraguado normal para construcción", 'precio': 8500,'imagen': "martillo.png", 'stock': 200,'categoria': 1, 'marca': 1, 'proveedor': 1},
        {'nombre': "Ladrillo Fiscal 6 huecos2", 'descripcion': "Ladrillo cerámico estándar 6 huecos", 'precio': 350,'imagen': "martillo.png", 'stock': 1000,'categoria': 1, 'marca': 1, 'proveedor': 1},
        {'nombre': "Pintura Latex 4L2", 'descripcion': "Pintura blanca lavable interior/exterior", 'precio': 22900,'imagen': "martillo.png", 'stock': 30,'categoria': 1, 'marca': 1, 'proveedor': 1},
        {'nombre': "Cerámica 45x45 cm2", 'descripcion': "Piso cerámico antideslizante", 'precio': 8990,'imagen': "martillo.png", 'stock': 150},
        {'nombre': "Tubo PVC 1/2 x 3m2", 'descripcion': "Tubería para instalaciones sanitarias", 'precio': 3200,'imagen': "martillo.png", 'stock': 80,'categoria': 1, 'marca': 1, 'proveedor': 1},
        {'nombre': "Cable Eléctrico 2.5mm2", 'descripcion': "Cobre flexible para instalaciones", 'precio': 4500,'imagen': "martillo.png", 'stock': 120,'categoria': 1, 'marca': 1, 'proveedor': 1},
        {'nombre': "Interruptor Simple2", 'descripcion': "Interruptor de pared para 10A", 'precio': 2500,'imagen': "martillo.png", 'stock': 60,'categoria': 1, 'marca': 1, 'proveedor': 1},
        {'nombre': "Lijadora Orbital2", 'descripcion': "Lijadora profesional 250W con bolsa colectora", 'precio': 38900,'imagen': "martillo.png", 'stock': 12,'categoria': 1, 'marca': 1, 'proveedor': 1},
        {'nombre': "Nivel Laser2", 'descripcion': "Nivel láser autónivelante 360°", 'precio': 65900,'imagen': "NivelLaser360.jpg", 'stock': 5,'categoria': 1, 'marca': 1, 'proveedor': 1},
        {'nombre': "Andamio Modular2", 'descripcion': "Estructura metálica para trabajo en altura", 'precio': 125000,'imagen': "andamio.jpg", 'stock': 3,'categoria': 1, 'marca': 1, 'proveedor': 1},
        {'nombre': "Carretilla de Obra2", 'descripcion': "Carretilla metálica 6 pies cúbicos", 'precio': 45900,'imagen': "martillo.png", 'stock': 18,'categoria': 1, 'marca': 1, 'proveedor': 1},
        {'nombre': "Mezcladora de Pintura2", 'descripcion': "Accesorio para taladro para mezclar pintura", 'precio': 8900,'imagen': "martillo.png", 'stock': 25,'categoria': 1, 'marca': 1, 'proveedor': 1},
        {'nombre': "Broca para Concreto 1/222", 'descripcion': "Juego de brocas widia para concreto", 'precio': 12900,'imagen': "martillo.png", 'stock': 40,'categoria': 1, 'marca': 1, 'proveedor': 1},
        {'nombre': "Guantes de Seguridad2", 'descripcion': "Guantes anticorte nivel 5", 'precio': 9900,'imagen': "martillo.png", 'stock': 75,'categoria': 1, 'marca': 1, 'proveedor': 1},
        {'nombre': "Casco de Seguridad2", 'descripcion': "Casco con ajuste ergonómico y visera", 'precio': 7500,'imagen': "martillo.png", 'stock': 50,'categoria': 1, 'marca': 1, 'proveedor': 1}
    ]
    
    for prod in productos_iniciales2:
        if not Productos.objects.filter(nombre=prod['nombre']).exists():
            Productos.objects.create(**prod)




def catalogoCompra(request):
    crear_productos_iniciales2()
    # Obtener parámetros GET
    orden = request.GET.get('orden', 'id')  # Orden por defecto 'id'
    categoria_id = request.GET.get('categoria', '')  # Puede ser '' o 'none' o id
    marca_id = request.GET.get('marca', '')
    proveedor_id = request.GET.get('proveedor', '')

    productos = Productos.objects.all()

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

    usuario = None

    if 'usuario_id' in request.session:
        try:
            usuario = Usuario.objects.get(id=request.session['usuario_id'])
        except Usuario.DoesNotExist:
            usuario = None

    return render(request, 'catalogoCompra.html', {
        'productos': productos,
        'categorias': categorias,
        'marcas': marcas,
        'proveedores': proveedores,
        'orden_seleccionado': orden,
        'categoria_seleccionada': categoria_id,
        'marca_seleccionada': marca_id,
        'proveedor_seleccionado': proveedor_id,
        'usuario': usuario,             
    })




def verPedido(request, producto_id=None):
    usuario = None
    if 'usuario_id' in request.session:
        usuario = Usuario.objects.filter(id=request.session['usuario_id']).first()

    if request.method == "POST":
        if producto_id is not None:
            # Caso: se agrega desde un producto individual
            producto = get_object_or_404(Productos, pk=producto_id)
            cantidad = int(request.POST.get("cantidad", 1))
            proveedor = producto.proveedor if producto.proveedor else None

            orden = OrdenCompra.objects.create(proveedor=proveedor)

            ProductoOrdenado.objects.create(
                orden=orden,
                producto=producto,
                nombre_producto=producto.nombre,
                precio_unitario=producto.precio,
                cantidad=cantidad,
                proveedor_id=proveedor.id if proveedor else None,
                proveedor_nombre=proveedor.nombre if proveedor else None
            )

        else:
            # Caso: se viene desde el carrito
            carrito = request.session.get('carrito', {})

            if carrito:
                # Tomamos proveedor del primer producto como ejemplo
                primer_item = next(iter(carrito.values()))
                producto = get_object_or_404(Productos, pk=primer_item['id'])
                proveedor = producto.proveedor if producto.proveedor else None

                orden = OrdenCompra.objects.create(proveedor=proveedor)

                for item in carrito.values():
                    producto = get_object_or_404(Productos, pk=item['id'])

                    ProductoOrdenado.objects.create(
                        orden=orden,
                        producto=producto,
                        nombre_producto=producto.nombre,
                        precio_unitario=producto.precio,
                        cantidad=item['cantidad'],
                        proveedor_id=proveedor.id if proveedor else None,
                        proveedor_nombre=proveedor.nombre if proveedor else None
                    )

                # Vaciar el carrito
                del request.session['carrito']
                request.session.modified = True

        return redirect('verPedido')

    # GET: Mostrar las órdenes existentes
    ordenes = OrdenCompra.objects.all().prefetch_related('detalles').order_by('-fecha')

    for orden in ordenes:
        total = 0
        for detalle in orden.detalles.all():
            detalle.subtotal = detalle.cantidad * detalle.precio_unitario
            total += detalle.subtotal
        orden.total = total

    return render(request, 'verPedido.html', {
        'ordenes': ordenes,
        'usuario': usuario
    })


def detalle_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    historial_precios = HistorialPrecio.objects.filter(producto=producto)[:3]  # Últimos 3 precios
    return render(request, 'detalle_producto.html', {
        'producto': producto,
        'historial_precios': historial_precios
    })

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    cantidad = int(request.POST.get('cantidad', 1))

    if 'carrito' not in request.session:
        request.session['carrito'] = {}

    carrito = request.session['carrito']
    producto_key = str(producto_id)

    if producto_key in carrito:
        carrito[producto_key]['cantidad'] += cantidad
    else:
        carrito[producto_key] = {
            'id': producto.id,
            'nombre': producto.nombre,
            'precio': str(producto.precio),  # convertir a string
            'cantidad': cantidad
        }

    request.session.modified = True
    return redirect('ver_carrito')

from .models import Producto  # o Productos según tu modelo

def ver_carrito(request):
    carrito = request.session.get('carrito', {})

    productos_ids = [int(k) for k in carrito.keys()]
    productos = Producto.objects.filter(id__in=productos_ids)

    items = []
    total = 0

    for key, item in carrito.items():
        item['id'] = int(key)  # convertir string a int aquí
        total += float(item['precio']) * item['cantidad']
        items.append(item)

    return render(request, 'carrito.html', {
        'items': items,
        'productos': productos,
        'total': total,
    })



def vaciar_carrito(request):
    if 'carrito' in request.session:
        del request.session['carrito']
    return redirect('ver_carrito')

from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from .models import Proveedor

def deshabilitar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    proveedor.activo = False
    proveedor.save()
    return redirect(reverse('proveedor'))

def habilitar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    proveedor.activo = True
    proveedor.save()
    return redirect(reverse('proveedor'))


def bajoStock(request):

    usuario_actual = request.session.get('usuario_id')

    usuario = Usuario.objects.filter(id=usuario_actual).first()

    productos = Producto.objects.filter(stock__lte=5)  
    fecha_alerta = date.today()

    return render(request, 'bajoStock.html', {
        'productos': productos,
        'fecha_alerta': fecha_alerta,
        'usuario': usuario
    })


def cerrar_sesion(request):
    try:
        del request.session['usuario_id']  
    except KeyError:
        pass
    return redirect('login')  
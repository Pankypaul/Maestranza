from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('agregarProducto/', views.agregarProducto, name='agregarProducto'),
    path('agregarCategoria/', views.agregarCategoria, name='agregarCategoria'),
    path('agregarMarca/', views.agregarMarca, name='agregarMarca'),
    path('agregarProveedor/', views.agregarProveedor, name='agregarProveedor'),
    path('editarProducto/<int:producto_id>/', views.editarProducto, name='editarProducto'),
    path('eliminarProducto/<int:producto_id>/', views.eliminarProducto, name='eliminarProducto'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('eliminarUsuario/<int:usuario_id>/', views.eliminarUsuario, name='eliminarUsuario'),
    path('editarUsuario/<int:usuario_id>/', views.editarUsuario, name='editarUsuario'),
    path('proveedor/', views.proveedores_view, name='proveedor'),
    path('proveedor/editar/<int:id>/', views.editar_proveedor, name='editar_proveedor'),
    path('proveedor/eliminar/<int:id>/', views.eliminar_proveedor, name='eliminar_proveedor'),
    path('catalogoCompra/', views.catalogoCompra, name='catalogoCompra'),
    path('producto2/<int:producto_id>/', views.detalle_productos, name='detalle_productos'),
    path('verPedido/', views.verPedido, name='verPedido'),
    path('verPedido/<int:producto_id>/', views.verPedido, name='verPedido'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('agregar-al-carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('vaciar-carrito/', views.vaciar_carrito, name='vaciar_carrito'),
    path('proveedores/deshabilitar/<int:proveedor_id>/', views.deshabilitar_proveedor, name='deshabilitar_proveedor'),
    path('proveedores/habilitar/<int:proveedor_id>/', views.habilitar_proveedor, name='habilitar_proveedor'),


]

    
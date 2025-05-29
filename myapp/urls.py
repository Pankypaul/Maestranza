from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('admin-panel/', views.admin_panel, name='admin-panel-demo'),
    path('agregarProducto/', views.agregarProducto, name='agregarProducto'),
    path('agregarCategoria/', views.agregarCategoria, name='agregarCategoria'),
    path('agregarMarca/', views.agregarMarca, name='agregarMarca'),
    path('agregarProveedor/', views.agregarProveedor, name='agregarProveedor'),
    ]
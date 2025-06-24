from django import forms
from .models import Proveedor
from .models import Marca
from .models import Categoria
from .models import Producto
from .models import Usuario
from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'imagen', 'stock', 'categoria', 'marca', 'proveedor']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'marca': forms.Select(attrs={'class': 'form-control'}),
            'proveedor': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre', '').strip()
        if not nombre:
            raise forms.ValidationError("El nombre es obligatorio.")
        if len(nombre) > 100:
            raise forms.ValidationError("El nombre no puede superar los 100 caracteres.")
        return nombre

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion', '').strip()
        if len(descripcion) > 500:
            raise forms.ValidationError("La descripción no puede superar los 500 caracteres.")
        return descripcion

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock is None:
            raise forms.ValidationError("El stock es obligatorio.")
        if stock < 0:
            raise forms.ValidationError("El stock no puede ser negativo.")
        return stock

    def clean_categoria(self):
        categoria = self.cleaned_data.get('categoria')
        if not categoria:
            raise forms.ValidationError("Debe seleccionar una categoría.")
        return categoria

    def clean_marca(self):
        marca = self.cleaned_data.get('marca')
        if not marca:
            raise forms.ValidationError("Debe seleccionar una marca.")
        return marca

    def clean_proveedor(self):
        proveedor = self.cleaned_data.get('proveedor')
        if not proveedor:
            raise forms.ValidationError("Debe seleccionar un proveedor.")
        return proveedor




class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la categoría'}),
        }




class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la marca'}),
        }





from django import forms
from .models import Proveedor
import re

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'correo', 'telefono', 'direccion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre', '').strip()
        if not nombre:
            raise forms.ValidationError("El nombre es obligatorio.")
        if len(nombre) > 100:
            raise forms.ValidationError("El nombre no puede tener más de 100 caracteres.")
        return nombre

    def clean_correo(self):
        correo = self.cleaned_data.get('correo', '').strip()
        if not correo:
            raise forms.ValidationError("El correo es obligatorio.")
        return correo

    def clean_direccion(self):
        direccion = self.cleaned_data.get('direccion', '').strip()
        if not direccion:
            raise forms.ValidationError("La dirección es obligatoria.")
        if len(direccion) > 200:
            raise forms.ValidationError("La dirección no puede tener más de 200 caracteres.")
        return direccion



class EditarProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'imagen', 'stock', 'categoria', 'marca', 'proveedor']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }






class UsuarioForm(forms.ModelForm):
    contrasena = forms.CharField(
        widget=forms.PasswordInput,
        label="Contraseña"
    )

    class Meta:
        model = Usuario
        fields = ['nombre', 'telefono', 'correo', 'contrasena', 'tipo_id']
        widgets = {
            'nombre': forms.TextInput(attrs={'maxlength': 100}),
            'telefono': forms.TextInput(attrs={'maxlength': 15}),
            'correo': forms.EmailInput(),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre', '').strip()
        if not nombre:
            raise forms.ValidationError("El nombre es obligatorio.")
        if len(nombre) > 100:
            raise forms.ValidationError("El nombre no puede tener más de 100 caracteres.")
        return nombre

    def clean_correo(self):
        correo = self.cleaned_data.get('correo', '').strip()
        if not correo:
            raise forms.ValidationError("El correo es obligatorio.")
        if Usuario.objects.filter(correo=correo).exists():
            raise forms.ValidationError("Este correo ya está registrado.")
        return correo

    def clean_contrasena(self):
        contrasena = self.cleaned_data.get('contrasena', '')
        if not contrasena:
            raise forms.ValidationError("La contraseña es obligatoria.")
        if len(contrasena) < 6:
            raise forms.ValidationError("La contraseña debe tener al menos 6 caracteres.")
        return contrasena



class LoginForm(forms.Form):
    correo = forms.EmailField(label="Correo")
    contrasena = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

class EditarUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'telefono', 'correo', 'contrasena', 'tipo_id']

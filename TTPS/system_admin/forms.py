from inicio_sesion.models import Usuario
from medicos.models import Medico
from lab_admin.models import Centro, Lugar
from django import forms
import secrets
import string

class UsuarioForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        input_formats=['%Y-%m-%d']
    )
    
    class Meta:
        model = Usuario
        fields = ['dni', 'first_name', 'last_name', 'fecha_nacimiento', 'email']
        widgets = {
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True, rol=None):
        usuario = super().save(commit=False)
        usuario.username = usuario.dni
        if rol:
            usuario.rol = rol
        
        caracteres = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(caracteres) for _ in range(12))
        usuario.set_password(password)
        
        if commit:
            usuario.save()

        return usuario, password
    

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['especialidad', 'matricula']
        widgets = {
            'especialidad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Especialidad',
                'maxlength': '100',
            }),
            'matricula': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Matrícula',
                'maxlength': '50',
            }),
        }
        labels = {
            'especialidad': 'Especialidad Médica',
            'matricula': 'Matrícula Profesional',
        }

class CentroForm(forms.ModelForm):
    class Meta:
        model = Centro
        fields = ['nombre', 'provincia', 'localidad','direccion', 'longitud', 'latitud', 'telefono', 'email']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del Centro',
                'maxlength': '100',
            }),
            'provincia': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Provincia',
                'maxlength': '150',
            }),
            'localidad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Localidad',
                'maxlength': '150',
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Dirección',
                'maxlength': '150',
            }),
            'longitud': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Longitud',
                'step': '0.000001',
            }),
            'latitud': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Latitud',
                'step': '0.000001',
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Teléfono',
                'maxlength': '20',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Correo Electrónico',
            }),
        }
        labels = {
            'nombre': 'Nombre del Centro',
            'provincia': 'Provincia',
            'localidad': 'Localidad',
            'direccion': 'Dirección',
            'longitud': 'Longitud (Geolocalización)',
            'latitud': 'Latitud (Geolocalización)',
            'telefono': 'Teléfono de Contacto',
            'email': 'Correo Electrónico'
        }


class LugarForm(forms.ModelForm):
    class Meta:
        model = Lugar
        fields = ['ciudad', 'provincia', 'pais']
        widgets = {
            'ciudad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la ciudad',
                'maxlength': 100,
            }),
            'provincia': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la provincia',
                'maxlength': 100,
            }),
            'pais': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el país',
                'maxlength': 100,
            }),
        }
        labels = {
            'ciudad': 'Ciudad',
            'provincia': 'Provincia',
            'pais': 'País',
        }

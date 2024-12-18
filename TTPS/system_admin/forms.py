from inicio_sesion.models import Usuario
from medicos.models import Medico
from lab_admin.models import LabAdmin
from lab_admin.models import Centro
from django import forms

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
        usuario.rol = rol
        usuario.set_password(str(usuario.dni))
        
        if commit:
            usuario.save()

        return usuario

class UsuarioRolForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        input_formats=['%Y-%m-%d']
    )
    
    class Meta:
        model = Usuario
        fields = ['dni', 'first_name', 'last_name', 'fecha_nacimiento', 'email', 'rol']
        widgets = {
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
    
    def save(self, commit=True, rol=None):
        usuario = super().save(commit=False)
        usuario.username = usuario.dni
        usuario.rol = rol
        usuario.set_password(str(usuario.dni))
        
        if commit:
            usuario.save()

        return usuario
    
class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['especialidad', 'matricula']

class CentroForm(forms.ModelForm):
    class Meta:
        model = Centro
        fields = ['nombre', 'direccion', 'longitud', 'latitud', 'telefono', 'email']
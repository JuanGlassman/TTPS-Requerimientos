from django import forms

class LoginForm(forms.Form):
    dni = forms.CharField(
        label="DNI",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su DNI'
        })
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su Contraseña'
        })
    )


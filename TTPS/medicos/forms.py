from django import forms
from pacientes.models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['antecedentes', 'historial_medico']
        widgets = {
            'antecedentes': forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Escribe aquí los antecedentes relevantes del paciente",
            }),
            'historial_medico': forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Describe el historial médico del paciente",
            }),
        }


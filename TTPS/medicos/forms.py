from django import forms

class PacienteForm(forms.Form):
    # Datos del paciente
    antecedentes = forms.CharField(
        max_length=150,
        required=False,
        label="Antecedentes médicos",
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 3,
            "placeholder": "Escribe aquí los antecedentes relevantes del paciente",
        })
    )
    historial_medico = forms.CharField(
        max_length=150,
        required=False,
        label="Historial médico",
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 3,
            "placeholder": "Describe el historial médico del paciente",
        })
    )


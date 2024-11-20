from django import forms
from lab_admin.models import Turno

class TurnoForm(forms.ModelForm):
    horario = forms.ChoiceField(label="Horario disponible", widget=forms.Select)

    class Meta:
        model = Turno
        fields = ['centro', 'fecha', 'horario', 'consentimiento']

    def __init__(self, *args, **kwargs):
        horarios_disponibles = kwargs.pop('horarios_disponibles', [])
        super().__init__(*args, **kwargs)
        self.fields['horario'].choices = [(h, h) for h in horarios_disponibles]


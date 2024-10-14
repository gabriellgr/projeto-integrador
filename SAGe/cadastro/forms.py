from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'email', 'data_de_nascimento', 'cpf', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
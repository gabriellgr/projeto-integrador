from django import forms
from django.utils import timezone
from django.utils.timezone import timedelta
from agendamentos.models import AgendamentoConsulta

def validate_medic_data(value):
    if AgendamentoConsulta.objects.filter(medico=medico, data=data_consulta, hora=hora_consulta).exists():
            raise forms.ValidationError(f"O médico {medico.nome} já tem uma consulta agendada para este horário.")
            return redirect('agendar_consulta')
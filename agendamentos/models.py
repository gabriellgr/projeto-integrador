from django.db import models
from medicos.models import Medico
from pacientes.models import Paciente

class AgendamentoConsulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()
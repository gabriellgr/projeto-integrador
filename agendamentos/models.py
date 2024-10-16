from django.db import models
from pacientes.models import Pacientes
from medicos.models import Medicos

class AgendamentoConsulta(models.Model):
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medicos, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()

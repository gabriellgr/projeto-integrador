from django.db import models

class Medicos(models.Model):
    id_medico = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    telefone = models.TextField(max_length=15)
    crm = models.CharField(max_length=20, unique=True, null=True)  # CRM do médico
    especialidade = models.CharField(max_length=100, null=True)  # Especialidade do médico
    email = models.EmailField(max_length=255, null=True, blank=True)  # Email opcional
    
    def __str__(self):
        return f"{self.nome} - {self.especialidade}"


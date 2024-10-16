from django.db import models

# Create your models here.

class Pacientes(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField(null=True, blank=True)
    cpf = models.TextField(unique=True)
    telefone = models.TextField(max_length=15)

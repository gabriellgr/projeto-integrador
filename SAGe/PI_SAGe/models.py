from django.db import models

class Pacientes(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()
    cpf = models.TextField(unique=True)
    data_consulta = models.DateField()
    senha = models.CharField(max_length=128) # Define o tipo CharField para armazenar a senha 
    telefone = models.TextField(max_length=15)

class Medicos(models.Model):
    id_medico = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    data_disponivel = models.DateField()
    telefone = models.TextField(max_length=15)
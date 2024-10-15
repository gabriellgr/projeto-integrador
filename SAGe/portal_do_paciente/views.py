from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
'''import os
from  dotenv import load_dotenv

# Caminho absoluto para a pasta onde o arquivo .env está localizado

#exemplo: caminho_env = "C:\\Users\\Lucas\\Desktop\\projeto-SAge\\.env"

# Carrega o arquivo .env
load_dotenv(dotenv_path=caminho_env)
load_dotenv('projeto/.env')

USERNAME = os.getenv('name')
PASSWORD = os.getenv('password')
'''

# Create your views here.

def portal_do_paciente(request, id):
    context = {
        #'name':USERNAME,
        #'password':PASSWORD,
        'id':id
    }
    return render(request, 'portal_do_paciente.html',context)  # Adiciona o 'id' ao contexto

def atendimento(request, id):  # Adiciona o argumento id à view
    # ... 

    return render(request, 'atendimento.html', {'id': id})  # Adiciona o 'id' ao contexto
def medicos(request, id):  # Adiciona o argumento id à view
    # ... 

    return render(request, 'medicos.html', {'id': id})  # Adiciona o 'id' ao contexto
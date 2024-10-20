from django.contrib.auth.models import User
from django.http import HttpResponse
from cadastro.models import Paciente
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from datetime import datetime

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

@login_required
def portal_do_paciente(request, id):
    DATA = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    
    # Verifique se o usuário tem permissão para acessar os dados do paciente
    if request.user.id != int(id):  # Converta o id para inteiro e compare
        return redirect('login')  # Redirecione para a página de login

    IS_ADMIN = False
    paciente = Paciente.objects.get(id=int(id))  # Obtenha o paciente
    FIRST_NAME =  paciente.nome.split()[0].title()
    
    if paciente.nome == 'admin':
        IS_ADMIN = True
        
    #print('Tipo de variavel - nome - senha ')
    #print(type(IS_ADMIN), type(paciente.nome), type(paciente.password))
    #print(IS_ADMIN, paciente.nome, paciente.password)
    context = {
        'paciente': paciente,  # Adicione o objeto paciente ao contexto
        'data':DATA, # Data
        'admin': IS_ADMIN,
        'name': FIRST_NAME,
    }
    return render(request, 'portal_do_paciente.html', context)

def cadastro_de_medicos(request, id):
    paciente = Paciente.objects.get(id=int(id))  # Obtenha o paciente
    context = {
        'paciente': paciente,  # Adicione o objeto paciente ao contexto
    }
    return render(request, 'cadastrar_medicos.html', context)

'''
def atendimento(request, id):  # Adiciona o argumento id à view
    # ... 

    return render(request, 'atendimento.html', {'id': id})  # Adiciona o 'id' ao contexto
def medicos(request, id):  # Adiciona o argumento id à view
    # ... 

    return render(request, 'medicos.html', {'id': id})  # Adiciona o 'id' ao contexto
    
    '''
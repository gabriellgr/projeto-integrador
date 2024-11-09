from pacientes.models import Paciente
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from datetime import datetime
from medicos.models import Medico
from agendamentos.models import AgendamentoConsulta

@login_required
def portal_do_paciente(request, id):
    DATA = datetime.now()
    
    # Verifique se o usuário tem permissão para acessar os dados do paciente
    if request.user.id != int(id):  # Converta o id para inteiro e compare
        return redirect('login')  # Redirecione para a página de login

    
    paciente = Paciente.objects.get(id=int(id))  # Obtenha o paciente
    medicos = Medico.objects.all()
    agendamentos = AgendamentoConsulta.objects.all()

    try:
        FIRST_NAME =  paciente.nome.split()[0].title()
    except:
        FIRST_NAME =  "Not found"
    
    #A fazer ...
    IS_ADMIN = False
    if paciente.nome == 'admin':
        IS_ADMIN = True
        

    #Variaves passadas ao template
    context = {
        'paciente': paciente,  # Adicione o objeto paciente ao contexto
        'data':DATA, # Data
        'admin': IS_ADMIN,
        'name': FIRST_NAME,
        'medicos':medicos,
        'agendamentos':agendamentos,
    }
    return render(request, 'portal_do_paciente.html', context)

@login_required
def cadastro_de_medicos(request, id):
    if request.user.id != int(id):  # Converta o id para inteiro e compare
        return redirect('login')  # Redirecione para a página de login
    else:
        paciente = Paciente.objects.get(id=int(id))  # Obtenha o paciente
        context = {
            'paciente': paciente,  # Adicione o objeto paciente ao contexto
        }
        return render(request, 'cadastrar_medicos.html', context)


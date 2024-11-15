from pacientes.models import Paciente
from medicos.models import Medico
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from datetime import datetime,time
from django.contrib import messages
from django.contrib.auth import logout
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


from datetime import datetime

@login_required
def agendar_consulta(request, id):
    if request.user.id != int(id):
        return redirect('login')  
    try:
        paciente = Paciente.objects.get(id=id)
    except Paciente.DoesNotExist:
        return redirect('cadastro')

    if request.method == 'POST':
        data_consulta = request.POST.get('data_consulta')  
        hora_consulta = request.POST.get('hora_consulta')
        id_medico = request.POST.get('id_medico')

        if not data_consulta or not hora_consulta or not id_medico:
            messages.error(request, "Todos os campos são obrigatórios.")
            return redirect('agendar_consulta', id=id)

        try:
            medico = Medico.objects.get(id=id_medico)
        except Medico.DoesNotExist:
            messages.error(request, "Médico inválido.")
            return redirect('agendar_consulta', id=id)

        # Conversão de string para datetime.time
        try:
            hora_consulta = datetime.strptime(hora_consulta, '%H:%M').time()
        except ValueError:
            messages.error(request, "Formato de horário inválido.")
            return redirect('agendar_consulta', id=id)

        if AgendamentoConsulta.objects.filter(medico=medico, data=data_consulta, hora=hora_consulta).exists():
            messages.error(request, f"O médico {medico.nome} já tem uma consulta agendada para este horário.")
            return redirect('agendar_consulta', id=id)

        AgendamentoConsulta.objects.create( 
            paciente=paciente,
            medico=medico,
            data=data_consulta,
            hora=hora_consulta
        )

        messages.success(request, "Consulta agendada com sucesso!")
        return redirect('portal_do_paciente', id=id)

    medicos = Medico.objects.all()
    HORARIOS_DICT = {
        "08:00": "08:00 às 09:00", 
        "09:00": "09:00 às 10:00", 
        "10:00": "10:00 às 11:00", 
        "11:00": "11:00 às 12:00", 
        "12:00": "12:00 às 13:00", 
        "13:00": "13:00 às 14:00"
    }
    context = {
        'paciente': paciente,
        'medicos': medicos,
        'horarios': HORARIOS_DICT
    }
    return render(request, 'agendamento.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirecione para a página de login

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

@login_required
def gestao_de_pacientes(request, id):
    if request.user.id != int(id):  # Converta o id para inteiro e compare
        return redirect('login')  # Redirecione para a página de login
    else:
        paciente_all = Paciente.objects.all()
        paciente = Paciente.objects.get(id=int(id))  # Obtenha o paciente
        context = {
            'paciente': paciente,  # Adicione o objeto paciente ao contexto
            'pacientes':paciente_all,
        }
        return render(request, 'gerenciar_pacientes.html', context)

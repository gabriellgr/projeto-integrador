from pacientes.models import Paciente
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from datetime import datetime
from medicos.models import Medico
from django.contrib import messages
from agendamentos.models import AgendamentoConsulta
from django.contrib.auth import logout




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

        # Buscar o médico selecionado
        try:
            medico = Medico.objects.get(id=id_medico)
        except Medico.DoesNotExist:
            messages.error(request, "Médico inválido.")
            return redirect('agendar_consulta', id=id)

        # Verificar se o médico já tem uma consulta naquele horário
        if AgendamentoConsulta.objects.filter(medico=medico, data=data_consulta, hora=hora_consulta).exists():
            messages.error(request, f"O médico {medico.nome} já tem uma consulta agendada para este horário.")
            return redirect('agendar_consulta', id=id)

        # Criar o agendamento
        AgendamentoConsulta.objects.create( 
            paciente=paciente,
            medico=medico,
            data=data_consulta,
            hora=hora_consulta
        )

        messages.success(request, "Consulta agendada com sucesso!")
        return redirect('portal_do_paciente', id=id) # Passa o id do paciente para a rota

    medicos = Medico.objects.all()  # Listar médicos para o formulário

    #variaveis passadas ao html
    context = {
        'paciente': paciente,
        'medicos': medicos,
    }

    return render(request, 'agendamento.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirecione para a página de login

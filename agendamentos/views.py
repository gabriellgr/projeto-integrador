from django.shortcuts import render, redirect
from django.contrib import messages
from .models import AgendamentoConsulta
from pacientes.models import Pacientes
from medicos.models import Medicos

def agendar_consulta(request):
    if request.method == 'POST':
        nome_paciente = request.POST.get('nome_paciente')
        cpf = request.POST.get('cpf')
        data_consulta = request.POST.get('data_consulta')
        hora_consulta = request.POST.get('hora_consulta')
        id_medico = request.POST.get('id_medico')

        # Validação básica de campos obrigatórios
        if not nome_paciente or not cpf or not data_consulta or not hora_consulta or not id_medico:
            messages.error(request, "Todos os campos são obrigatórios.")
            return redirect('agendar_consulta')

        # Verificar se o paciente já está cadastrado
        try:
            paciente = Pacientes.objects.get(cpf=cpf)
        except Pacientes.DoesNotExist:
            paciente = Pacientes.objects.create(nome=nome_paciente, cpf=cpf)

        # Buscar o médico selecionado
        try:
            medico = Medicos.objects.get(id_medico=id_medico)
        except Medicos.DoesNotExist:
            messages.error(request, "Médico inválido.")
            return redirect('agendar_consulta')

        # Verificar se o médico já tem uma consulta naquele horário
        if AgendamentoConsulta.objects.filter(medico=medico, data=data_consulta, hora=hora_consulta).exists():
            messages.error(request, f"O médico {medico.nome} já tem uma consulta agendada para este horário.")
            return redirect('agendar_consulta')

        # Criar o agendamento
        AgendamentoConsulta.objects.create(
            paciente=paciente,
            medico=medico,
            data=data_consulta,
            hora=hora_consulta
        )

        messages.success(request, "Consulta agendada com sucesso!")
        return redirect('listar_agendamentos')

    # Carregar a página de agendamento
    medicos = Medicos.objects.all()  # Listar médicos para o formulário
    return render(request, 'cadastro_agendamento.html', {'medicos': medicos})

def redirecionar_para_agendamentos(request):
    return redirect('agendar_consulta')  
- Você é um especialita em django e precisa criar um sistema de agendamento
- Para isso você precisa conciliar este models, views e html:
- Com este arquivos modele models, html e views no que for necessário
para que funcione a inserção de dados corretamente, veja que os horarios estão em formato de tupla, mas é mais covniente passar como tipo dicionario. Observe também o formato da data na hora de salvar, avalie bém o class AgendamentoConsulta.
- models
```python
from django.db import models
from medicos.models import Medico
from pacientes.models import Paciente
from datetime import time

class AgendamentoConsulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    
    HORARIOS = (
        (time(8, 0), "08:00 às 09:00"),
        (time(9, 0), "09:00 às 10:00"),
        (time(10, 0), "10:00 às 11:00"),
        (time(11, 0), "11:00 às 12:00"),
        (time(12, 0), "12:00 às 13:00"),
        (time(13, 0), "13:00 às 14:00"),
    )
    
    data = models.DateField()
    hora = models.TimeField(
        choices=HORARIOS, default=time(8, 0)
    )

    def __str__(self):
        return f"Consulta de {self.paciente} com {self.medico} em {self.data} às {self.hora}"```
```

```python
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
```

- html

```
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Agendamento de Consultas</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>

    <!-- Barra de Navegação -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Agendamento</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    
                    <li class="nav-item">
                        <a class="btn btn-danger" href="{% url 'portal_do_paciente' id=paciente.id %}">Voltar</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Container do Formulário -->
    <div class="container mt-5">
        <h1>Agendar Consulta</h1>
        <form method="POST" >
            {% csrf_token %}
            <div class="mb-3">
                <label for="dataConsulta" class="form-label">Data da Consulta</label>
                <input type="date" class="form-control" id="dataConsulta" name="data_consulta" required>
            </div>
            <div class="mb-3">
                <label for="horaConsulta" class="form-label">Hora da Consulta</label>
                <select type="time" class="form-control" id="hora_consulta" name="hora_consulta" required>
                    <option value="" selected disabled>Horário</option>
                    {% for key, value in horarios.items %}
                        <option value="{{ key }}">{{ value }}</option>
                    {% endfor %}
                </select>
            </div>
            <div class="mb-3">
                <label for="medico" class="form-label">Médico</label>
                <select class="form-select" id="medico" name="id_medico" required>
                    <option value="" selected disabled>Selecione o Médico</option>
                    <!-- Valores preenchidos dinamicamente com Django -->
                    {% for medico in medicos %}
                        <option value="{{ medico.id }}">{{ medico.nome }} - {{ medico.especialidade }}</option>
                    {% endfor %}
                </select>
            </div>

            <button type="submit" class="btn btn-primary">Agendar Consulta</button>
        </form>
    </div>
    
    {% if messages %}
    <ul class="messages">
        {% for message in messages %}
            <li{% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message }}</li>
        {% endfor %}
    </ul>
    {% endif %}

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```
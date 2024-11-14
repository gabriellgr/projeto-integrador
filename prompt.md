### Você é um expert em django e precisa realizar o gerencimento de logins
- Como você vai realizar o login para estas paginas?

- veja a pagina views.py:

```python
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from pacientes.forms import PacienteForm
from pacientes.models import Paciente

def remover_formatacao_cpf(cpf:str = '123.456.789-10'):
  """
  Remove pontos e traços de um CPF formatado.

  Args:
      cpf: O CPF formatado (ex: '123.456.789-00').

  Returns:
      O CPF sem formatação (ex: '12345678900').
  """
  return cpf.replace('.', '').replace('-', '')



def home(request):
    context ={
        #'paciente':paciente,#Chama-se com a chave, não o valor
    }

    return render(request, 'home.html')

def _login_(request):
    
    """
    View para efetuar o login de um paciente.
    """
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        password = request.POST.get('password')

        print(password)
        print(cpf)
        # Autentica o usuário usando CPF (definido como username no modelo) e senha
        user = authenticate(username=cpf, password=str(password)) 
        print(user)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('portal_do_paciente', id=user.id)  # Redireciona para o portal do paciente
        else:
            messages.error(request, 'CPF ou senha inválidos!')
            return render(request, 'login.html')

    return render(request, 'login.html')

def cadastro(request):
    """
    View para cadastrar um novo paciente.
   """
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            # Cria o novo paciente no banco de dados
            print(form)
            paciente = form.save(commit=False)  # Cria o objeto Paciente, mas não salva ainda
            
            # Define a senha usando set_password
            paciente.set_password(form.cleaned_data['password'])

            # Define a data de nascimento corretamente
            paciente.data_de_nascimento = form.cleaned_data['data_de_nascimento']
            
            # Salva o paciente no banco de dados
            paciente.is_staff = False
            paciente.is_superuser = False
            paciente.is_active = True
    
            paciente.save()

            # Faz o login do paciente recém-cadastrado
            login(request, paciente) 
            messages.success(request, 'Paciente cadastrado com sucesso!')

            return redirect('login')  # Redireciona para a página inicial após o cadastro
        else:
            # Imprime os erros do formulário para debugging
            print(form.errors)
            return render(request, 'cadastro.html', {'form': form})
    else:
        form = PacienteForm()
    return render(request, 'cadastro.html', {'form': form})

def _cadastrar_medicos(request):
    return render(request, 'cadastrar_medicos.html')
    
    
'''def login(request):
    """
    View para efetuar o login de um paciente.
    """
    if request.method == 'POST':
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        password = request.POST.get('password')
        # Autentica o usuário
        user = authenticate(email=email, password=password, cpf=cpf)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('home')  # Redireciona para a página inicial após o login
        else:
            messages.error(request, 'Email, CPF ou senha inválidos!')
    return render(request, 'cadastro/login_paciente.html')

def home(request):
    """
    View para a página inicial, acessível somente para usuários autenticados.
    """
    if request.user.is_authenticated:
        return render(request, 'cadastro/home.html')
    else:
        return redirect('login')  # Redireciona para a tela de login se o usuário não estiver autenticado'''

def teste(request):
    return render(request, 'teste.html')

def view(request):
    return render(request, 'administracao.html')
```

- neste arquivo você deve realizar o login da seguinte forma: quando o usario entrar na pag ele tera a opção de cadastro login
e portal do paciente que só é permitida com o login. Tendo este problema como você lida-ra com isso? Como pode resolver de maneira pratica?

- Perceba que existem outro arquivo views de outro app:

```python
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

```
- Muito bém de acordo com estes códigos você é capaz de realizar as condições certas para:
    - usuario não logado: pode se cadastrar ou relizar login e entrar no portal do paciente
    - usuario sem cadastro pode se cadastrar, logar e entrar no portal do paciente
    - ambos após o login podem transitar entre portal do paciente e home, caso contrario
    devem ser redirecionados ao login.
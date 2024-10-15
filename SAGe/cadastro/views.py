from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import PacienteForm
from .models import Paciente

def cadastro(request):
    """
    View para cadastrar um novo paciente.
    """
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            # Cria o novo paciente no banco de dados
            paciente = form.save(commit=False)  # Cria o objeto Paciente, mas não salva ainda
            
            # Define a senha usando set_password
            paciente.set_password(form.cleaned_data['password'])

            # Define a data de nascimento corretamente
            paciente.data_de_nascimento = form.cleaned_data['data_de_nascimento']
            
            # Salva o paciente no banco de dados
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
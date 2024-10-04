from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from datetime import datetime
from .models import Pacientes, Medicos
from django.contrib.auth import authenticate, login


def tratar_palavra(palavra:str):
    palavra=list(palavra.lower())
    counter = 0
    
    for i in palavra:
        
        #vogais
        if i == "é" or i=='è'or i=='ê':
            palavra[counter]='e'
            
        if i == "á" or i=='à'or i=='â':
            palavra[counter]='a'
        
        if i == "í" or i=='ì'or i=='î':
            palavra[counter]='i'
            
        if i == "ó" or i=='ò'or i=='ô':
            palavra[counter]='o'
            
        if i == "ú" or i=='ù'or i=='û':
            palavra[counter]='u'
        #ponto
        if i =='.':
            palavra[counter]=''
        if i=="." or i=='-':
            palavra[counter]=''
            
        counter+=1
            
    print(''.join(palavra))
    
    return ''.join(palavra)

def home(request):
    return render(request, 'site_SAGe/home.html')

def portal_do_paciente(request):
    if request.method == 'POST':  # Verifica se o formulário foi enviado
        novo_usuario = Pacientes()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.idade = request.POST.get('idade')
        novo_usuario.cpf = tratar_palavra(request.POST.get('cpf'))
        novo_usuario.senha = request.POST.get('senha')
        novo_usuario.data_consulta = request.POST.get('data_consulta')
        novo_usuario.telefone = request.POST.get('telefone')
        novo_usuario.save()

        # Redireciona para a página de portal_do_paciente
        return redirect('portal_do_paciente')  # Adiciona o redirect aqui

    pacientes = Pacientes.objects.all()
    medicos = Medicos.objects.all()
    data_hora_atual = datetime.now() 
    
    context = {
        "pacientes":pacientes,
        "medicos":medicos,
        "data_hora":data_hora_atual,
    }
    
    return render(request, 'site_SAGe/portal_do_paciente.html', context ) 

def sobre(request):
    return render(request, 'site_SAGe/sobre.html')

#formulario
def cadastro(request):
    return render(request, 'site_SAGe/cadastro.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            cpf = form.cleaned_data.get('cpf-login')
            password = form.cleaned_data.get('senha-login')

            # Verifique se o usuário existe no banco de dados
            try:
                user = Pacientes.objects.get(cpf=cpf) 
            except Pacientes.DoesNotExist:
                form.add_error(None, 'CPF não encontrado.')
                return render(request, 'site_SAGe/login.html', {'form': form})

            # Verifique se a senha está correta
            if user.check_password(password):
                login(request, user)
                return redirect('portal_do_paciente') # Redireciona para a página do paciente
            else:
                form.add_error(None, 'Senha incorreta.')
                return render(request, 'site_SAGe/login.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'site_SAGe/login.html', {'form': form})

def admin_page(request):
    if request.method == 'POST':  # Verifica se o formulário foi enviado
        novo_usuario = Pacientes()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.idade = request.POST.get('idade')
        novo_usuario.cpf = request.POST.get('cpf')
        novo_usuario.senha = request.POST.get('senha')
        novo_usuario.data_consulta = request.POST.get('data_consulta')
        novo_usuario.telefone = request.POST.get('telefone')
        novo_usuario.save()

        # Redireciona para a página de portal_do_paciente
        return redirect('portal_do_paciente')  # Adiciona o redirect aqui

    pacientes = Pacientes.objects.all()
    medicos = Medicos.objects.all()
    data_hora_atual = datetime.now() 
    
    context = {
        "pacientes":pacientes,
        "medicos":medicos,
        "data_hora":data_hora_atual,
    }
    return render(request, 'site_SAGe/admin.html', context ) 

def cadastrar_medicos(request):
    return render(request, 'site_SAGe/cadastrar_medicos.html')
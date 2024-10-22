from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import get_user_model

def _login_(request):
    
    """
    View para efetuar o login de um paciente.
    """
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        password = request.POST.get('password')

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
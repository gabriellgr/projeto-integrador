from django.shortcuts import render

# Create your views here.

def home(request):

    context ={
        #'paciente':paciente,#Chama-se com a chave, não o valor
    }

    return render(request, 'home.html')

def teste(request):
    return render(request, 'teste.html')
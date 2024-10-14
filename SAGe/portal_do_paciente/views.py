from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.

def portal_do_paciente(request, id):
    return render(request, 'portal_do_paciente.html',)
        
    
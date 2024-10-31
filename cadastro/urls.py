from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    #path('portal_do_paciente/<int:id>/cadastro_de_medicos/', views._cadastrar_medicos, name='cadastro_de_medicos'),
    #path('login/cadastro_de_medicos/', views._cadastrar_medicos, name='cadastro_de_medicos'),
]
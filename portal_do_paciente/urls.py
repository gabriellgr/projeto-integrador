from . import views
from django.urls import path
from . views_set import (
    PacienteCreateView,
    PacienteDetailView,
    PacienteListView,
    PacienteSerializer
)

urlpatterns = [
    path('<int:id>/', views.portal_do_paciente, name='portal_do_paciente'), 
    path('<int:id>/cadastro_de_medicos/', views.cadastro_de_medicos, name='cadastro_de_medicos'),
    path('<int:id>', views.agendar_consulta, name='agendar_consulta'),
    #path('api/consultas/', PacienteSerializer.as_view(), name='consulta-list'),
    #path('api/consultas/<int:pk>/', PacienteDetailView.as_view(), name='consulta-detail'),
    #path('api/consultas/', PacienteCreateView.as_view(), name='consulta-create'), 
    path('api/consultas/', PacienteListView.as_view(), name='consulta-create'), 
]
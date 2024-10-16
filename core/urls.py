"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from agendamentos.views import redirecionar_para_agendamentos  # Importe a view de redirecionamento

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirecionar_para_agendamentos),  # Redireciona automaticamente ao acessar o root
    path('agendamentos/', include('agendamentos.urls')),  # Inclua as URLs do seu app
]

# Projeto Integrador FAP: Sistema de Agendamento e Gerenciamento de Consultas para JA Serviços Médicos LTDA (SAGe)

- Resumo: O SAGe é um sistema web desenvolvido em Python e Django para agendamento de consultas e gerenciamento de pacientes para a clínica médica JA Serviços Médicos LTDA. A plataforma proporcionará aos pacientes uma maneira fácil e
intuitiva de agendar consultas online, enquanto oferece à clínica uma ferramenta eficiente para organizar horários, gerenciar informações de pacientes e otimizar o fluxo de atendimento.

## Funcionalidades Principais ##
* Cadastro de pacientes e médicos
* Edição de usuários
* Agendamento de consultas
* Visualização de consultas agendadas
* Sistema de exclusão e cancelamento de consultas

## Requisitos para rodar o projeto

### Setup de ambiente:

- [Python](https://docs.python.org/3/)
- [Django](https://docs.djangoproject.com/en/)

### Como rodar na minha máquina?

- Clone o projeto  `git clone https://github.com/gabriellgr/projeto-integrador.git`
- Crie um ambiente virtual  `python -m venv venv`
- Ative o ambiente virtual  `.\venv\Scripts\activate`
- Instale os requisitos  `pip install -r requeriments.txt`
- Rode  `python manage.py migrate`
- Rode  `python manage.py createsuperuser` e cadastre seu usuário.

  Exemplo:
  ```
  Apelido/Usuário: admin
  E-mail: admin@email.com
  Password:
  Password (again):
  ```
- Inicie o servidor `python manage.py runserver`

Para visualizar se tudo está executando como o esperado, acesse o seguinte endereço: http://localhost:8000/


  ## Estrutura do projeto
  - `./core/` : É onde gerenciamos configurações e rotas do nosso projeto.
  - `./core/urls.py`: Configuramos nossas rotas.
  ``` Python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('home.urls')),  # Inclui as URLs do 'home'
        path('portal_do_paciente/', include('portal_do_paciente.urls')),  # Inclui as URLs do 'portal_do_paciente'
        path('agendamentos/', include('agendamentos.urls'))
    
    ]
  ``` 



  

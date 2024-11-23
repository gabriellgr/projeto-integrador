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

### Arquivos urls.py (Rotas):
- home/urls.py:
    ```python
    from django.urls import path, include
    from . import views


    urlpatterns = [
        path('', views.home, name='home'),
        path('cadastro/', views.cadastro, name = 'cadastro'),
        path('login/', views._login_, name='login'),
    ]
    ```
- portal_do_paciente/urls.py
    ```python
    from . import views
    from django.urls import path

    urlpatterns = [
        path('<int:id>/', views.portal_do_paciente, name='portal_do_paciente'), 
        path('<int:id>/cadastro_de_medicos/', views.cadastro_de_medicos, name='cadastro_de_medicos'),
        path('<int:id>/gestao_de_pacientes/', views.gestao_de_pacientes, name='gestao_de_pacientes'),
        path('<int:id>', views.agendar_consulta, name='agendar_consulta'),
        path('logout/', views.logout_view, name='logout'),
        path('paciente/<int:id>/editar/', views.editar_paciente, name='editar_paciente'),
        path('paciente/<int:id>/remover/', views.remover_paciente, name='remover_paciente'),
    ]
    ```

### models.py - Banco de dados (revisar)

- Arquivos onde ficam os "tabelas" criadas com  object relational model (ORM), neste projeto foi
utilizado o ORM nativo do Django. As principais tabelas criadas foram para os pacientes, medicos e 
o agendamentos. Ambos dividos por apps, com nomes: pacientes, medicos e agendamentos.

- O funcionamento acerca destes models é simples, paciente: que utiliza o serviço
e pode solicitar agendamentos para si mesmo, medico: o profissional que ficara disponível 
para seleção e escolha do usuário (paciente). E por fim angendamentos é responsável por unir ambos
para gerenciar melhor datas e horários de disponibilidade.





### Funções  que renderizam o template:

- Home/views.py;
- portal_do_paciente/views.py;

- Cada função têm como objetivo primário passar qual arquivo *.html* deve ser exibido,
o "nome" dado (rota) está no arquivo urls.py que deve ser exibido em seu navegador.No exemplo o 
arquivo passado é o *portal_do_paciente.html*. Na rota fica-rá:

http://127.0.0.1:8000/portal_do_paciente/

```python
return render(request, 'portal_do_paciente.html', context)
```

- Também é possível passar viariáveis python para o template o que forneçe
dinâmica e versátilidade.

```python
     #Variaves passadas ao template
    context = {
        'paciente': paciente,  # Adicione o objeto paciente ao contexto
        'data':DATA, # Data
        'admin': IS_ADMIN,
        'name': FIRST_NAME,
        'medicos':medicos,
        'agendamentos':agendamentos,
    }
```
- Essas variáveis são acessadas com uma linguagem específica
que mistura python ao arquivo html, exemplo:

```html
{% for medico in medicos %}
    <tr>
        <td>{{ medico.nome }}</td>
        <td>{{ medico.especialidade }}</td>
        <td>{{ medico.crm }}</td>
    </tr>
{% endfor %}

```

### As páginas web estão divididas nas pastas home/templates e portal_do_paciente/templates:
- Home/templates:
    - base.html
    - cadastro.html
    - home.html
    - login.html

- portal_do_paciente/templates
    - agendamentos.html
    - cadastrar_medicos.html
    - gerenciar_pacientes.html
    - portal_do_paciente.html
    - remover_paciente.html




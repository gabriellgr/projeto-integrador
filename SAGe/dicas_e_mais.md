 # Django
 
 ### Como rodar o programa:
- Na mesma pasta contendo o manage.py, depois de intalar o django faça no terminal (no caso, windows):
 ```cmd
 python .\manage.py runserver
 ```

 ### Como funciona, resumidamente:

 - **Funções para cada rota:** Na pasta *PI_SAGe* está o arquivo views.py que contêm as rotas dos arquivos.
```python
    from django.shortcuts import render

    def home(request):
        return render(request, 'site_SAGe/home.html')
```

- O arquivo home.html, como os, outros está localizado em: PI_SAGe/templates/site_SAGe/home.html. **Observação**: a pasta "templates" **obrigatoriamente** deve ter o nome "templates".

- **Definição das rotas:** SAGe/urls.py, onde colocamos as Urls.

```python
from django.urls import path
from PI_SAGe import views

urlpatterns = [
    path('', views.home, name='home'),  # URL base para a página inicial
    path('portal_do_paciente/', views.portal_do_paciente, name='portal_do_paciente'),
    path('sobre/', views.sobre, name='sobre'),
    path('cadastro/', views.cadastro, name='cadastro'),
    
]
```

- **Arquivos html:** Local PI_SAGe/templates/site_SAGe. Neste diretorio estão os arquivos: *home.html, cadastro.html, portal_do_paciente.html, sobre.html*. Os arquivos do programa.

### Extra:
- É indicado criar um ambiente virtual para iniciar um projeto no django para windows (existem outros modos também):
    ```cmd
        python -m venv <nome do ambiente virtual>
    ```
    - Para ativar
    ```cmd
        venv\Scripts\activate
        
    ```
    - para desativar:
    ```cmd
    deactivate
    ```

- Após criar o ambiente virtual
    ```cmd
    django-admin startproject <nome do projeto>
    ```
    - para criar um app:
    ```cmd
    django-admin startapp <nome do app>
    ```

- Após a criação do app é necessario coloca-lo no arquivo settings.py, como exemplo (PI_SAGe):


```python

    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'PI_SAGe'#Nome do app criado :)
]

```


### Arquivos estáticos [static (css, js, imagem)]:

- Se for usado arquivos como .css, .js ou mesmo imagens é necessário a criação da pasta "static"
na raiz do projeto (mesmo diretório do manage.py).

    - [Vídeo de auxilio](https://youtu.be/AWIJ2uMRjS0?feature=shared)

- no arquivo settings.py

``` python

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    
    os.path.join(BASE_DIR, 'static')#nome da pasta
]
```
- para carregar os arquivos no html.
```html
{% load static %}
```
- (control+f5)

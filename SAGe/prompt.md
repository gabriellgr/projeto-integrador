# para cada link presente em suamrio:
- crie uma mecîca com a qual toda vez que clicar no link deve aparecer a div correspondente e aclicar no x deve tornar o div invidivivelo(none) novamente, aplique esta mecaîca nops demasi links do sumario:

- css
```css
*{
    color:black;
    font-size: 1.2rem;
}
body{
    background:url('https://plus.unsplash.com/premium_photo-1682141162813-16fc10b5ba2f?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') ;
}

/*__________________header*/


/* Atualize o espaçamento da navbar para melhorar a aparência em dispositivos móveis */
.portal_do_paciente .navbar {
  background-color: gray !important;
  padding: 1rem;
  opacity: 0.8;
}

/* Estilo do texto da marca em dispositivos menores */
.portal_do_paciente .navbar-brand {
  font-size: 1.2rem;
  font-weight: bold;
}

/* Estilo dos links */
.portal_do_paciente .navbar-nav .nav-item .nav-link {
  color: #333;
  font-weight: 500;
}

/* Cor ao passar o mouse */
.portal_do_paciente .navbar-nav .nav-item .nav-link:hover {
  color: #007bff;
}

/*__________targets________*/
#lista_de_medicos{
    display: none;
}
#lista_de_medicos:target{
    position: absolute;
    top: 50%;
    left: 50%;
    padding: 10px;
    transform: translate(-50%, -50%);
    border-radius: 6px;
    background-color: #ddd;
    display: block;
}
#paciente{
    display: none;
}
#paciente:target{
    position: absolute;
    top: 50%;
    left: 50%;
    padding: 10px;
    transform: translate(-50%, -50%);
    border-radius: 6px;
    background-color: #ddd;
    display: block;
}
#historico{
    display: none;
}
#historico:target{
    padding: 10px;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    border-radius: 6px;
    background-color: #ddd;
    display: block;
}
#atendimento{
    display: none;
}

#atendimento:target{
    background-color: #ddd;
    display: block;
}

#consultas{
  display: none;
}
#consultas:target{
  
  padding: 10px;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    border-radius: 6px;
    background-color: #ddd;
  display: block;
}




/*_________ sumario*/
.nav-menu {
  background-color: #f2f2f2; /* Adiciona cor de fundo ao menu */
  padding: 20px;
  border-right: 1px solid #ddd; /* Adiciona uma borda direita */
  border-radius: 6px;
}

.nav-menu-link {
  display: block; /* Faz com que os links ocupem toda a largura */
  padding: 10px;
  text-decoration: none;
  color: #333;
  border-radius: 6px;
}
  .titulo_portal_do_paciente{
    text-align: center  !important;
  }
  .hora_data {
    text-align: right; 
    font-size: 1.2rem;
    color: #333; 
    font-weight: bold;
    
  }
  #div-data{
    text-align: end;
    margin-right: 30px;
    margin-top: -20px;
  }
  #data{
    font-weight:bolder;
  }
  /*--------------botoes*/
  .button-close{
    text-align: end;
  }

  #consultas-button-close,#pacientes-button-close,#historico-button-close,#atendimento-button-close{
    background-color: #333 !important;
    color: #fff;
    padding: 0px 13px 0px;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1.2rem;
    align-items: end;
  }
```
- html
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gerenciamento</title>
    
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link rel="stylesheet" href="{% static 'css/style_portal_do_paciente.css' %}">
    <script src="static/js/script_portal_do_paciente.js"></script>
</head>
<body>

  <header class="portal_do_paciente p-3">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container-fluid">
        <a class="navbar-brand" href="#"><strong>Home</strong></a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link" href="{% url 'home' %}">Home</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
</header>

  <!--
  <p >Olá, {{ username }}</p>
  {% if message %}
    <p style="font-size: 1.2rem;">{{ message }}</p>
  {% endif %}
  -->
  
  <h1 class="titulo_portal_do_paciente">Portal do paciente</h1>
  <div id="div-data">
    <time id="data" datetime="{{ data|date:'Y-m-d' }}">{{ data|date:'d/m/Y' }}</time>
  </div>
  
<!--<time class="hora_data" datetime="{{ data_hora|date:'Y-m-dTH:i:s' }}">{{ data_hora|date:'d/m/Y H:i' }}</time>-->
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-3">
        
        <nav class="nav-menu">
            
            <ol>
              <li><a class="nav-menu-link" href="#consultas">Consultas marcadas</a></li>        
              <li><a class="nav-menu-link" href="#atendimento">Marcar consulta</a></li>        
              <li><a class="nav-menu-link" href="#lista_de_medicos">Médicos disponíveis</a></li>
              <li><a class="nav-menu-link" href="#paciente">Meus dados</a></li>        
              <li><a class="nav-menu-link" href="#historico">Histórico de consultas</a></li>        
            </ol>
    
          </nav>     

      </div>

      <div class="col-md-9">

        <div id="lista_de_medicos">

            <h3>Horários e funções </h3>
            *FAZER*
             <strong>Lista de médicos, funções e horário de atendimento </strong>
      
             <table class="table table-custom">
                <thead>
                    <tr>
                        <th>Nome</th>
                        <th>Função</th>
                        <th>Consultas marcadas</th>
                    </tr>
                </thead>
                <tbody>
                    {% for medico in medicos %}
                        <tr>
                            <td>{{ medico.nome }}</td> 
                            <td>{{ medico.funcao }}</td>
                            <td>{{ medico.data_consulta }}</td> 
                        </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
      
      
        <div id="paciente">
          <h3>Seus dados</h3>
          <table class="table table-custom">
              <thead>
                  <tr>
                      <th>Id</th>
                      <th>Nome</th>
                      <th>Idade</th>
                      <th>CPF</th>
                      <th>Telefone</th>
                  </tr>
              </thead>
              <tbody>
                  {% for paciente in pacientes %}
                      {% if paciente.id_usuario == 3 %}
                          <tr>
                              <td>{{ paciente.id_usuario }}</td>
                              <td>{{ paciente.nome }}</td>
                              <td>{{ paciente.idade }}</td>
                              <td>{{ paciente.cpf }}</td>
                              <td>{{ paciente.telefone }}</td>        
                          </tr>
                      {% endif %}
                  {% endfor %}
              </tbody>
          </table>
      </div>
      
        <div id="historico">
            <h3>Baixe aqui seu histórico de consultas</h3>
            <a href="{% static 'historico/sage.pdf' %}" download="historico">Histórico</a>
        </div>
      
        <div id="atendimento">
          
          <h1>Solicite atendimento</h1>
      
          <div class="input-group rounded">
        
            <input id="pesquisa_especialidade" type="search" class="form-control rounded" placeholder="Pesquise a especialidade" aria-label="Search" aria-describedby="search-addon" />
      
      
            <span class="input-group-text border-0" id="search-addon">
              <i class="fas fa-search"></i>
            </span>
          </div>
          
         

        </div>
      
        <div id="consultas">
          <div class="button-close">
            <button id="consultas-button-close">x</button>
          </div>
          
          <h2>Suas consultas marcadas</h2>
          fazer vizualização
          <p>data: </p>
        </div>
      </div>

    </div>

  </div>

        <footer>
            <p>© 2024 Direitos Reservados Softex</p>
        </footer>
    

          
</body>
</html>
```
- se for necessrio pode usar javascript
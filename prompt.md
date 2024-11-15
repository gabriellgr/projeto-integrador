{% extends 'base.html' %}
{% load static %}

{% block title %}Cadastrar Médicos{% endblock %}

{% block content %}
  <link rel="stylesheet" href="{% static 'css/style_cadastrar_medicos.css' %}">

<header>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">
        <img src="{% static 'images/portal_do_paciente_icon.png' %}" alt="home" width="30" height="30">
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">  
          <li class="nav-item">
            <a class="nav-link" href="{% url 'portal_do_paciente' id=paciente.id %}">voltar</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</header>

<div class="container mt-5">
  <div class="row justify-content-center">
    <div class="col-md-8">
      <div class="card">
        <div class="card-body">
          <h2 class="card-title text-center">Cadastre um Médico</h2>
          <form method="post">
            {% csrf_token %}
            <div class="row">
              <div class="col-md-6">
                <div class="form-group">
                  <label for="nome">Nome:</label>
                  <input type="text" class="form-control" id="nome" name="nome_medico" required>
                </div>
              </div>
              <div class="col-md-6">
                <div class="form-group">
                  <label for="email">Email:</label>
                  <input type="email" class="form-control" id="email" name="email" required>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-md-6">
                <div class="form-group">
                  <label for="data_de_nascimento">Data de Nascimento:</label>
                  <input type="date" class="form-control" id="data_de_nascimento" name="data_de_nascimento" required>
                </div>
              </div>
              <div class="col-md-6">
                <div class="form-group">
                  <label for="cpf">CPF:</label>
                  <input type="text" class="form-control" id="cpf" name="cpf" required>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-md-6">
                <div class="form-group">
                  <label for="crm">CRM:</label>
                  <input type="number" class="form-control" id="crm" name="crm" required>
                </div>
              </div>
              <div class="col-md-6">
                <div class="form-group">
                  <label for="especialidade">Especialidade:</label>
                  <input type="text" class="form-control" id="especialidade" name="especialidade" required>
                </div>
              </div>
            </div>
            <div class="form-group">
              <label for="password">Senha:</label>
              <input type="password" class="form-control" id="password" name="password" required>
            </div>
            <button type="submit" class="btn btn-primary">Cadastrar</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</div>

{% endblock %}
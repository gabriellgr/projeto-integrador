document.addEventListener("DOMContentLoaded", function () {
  // Captura todos os links do sumário
  const links = document.querySelectorAll(".nav-menu-link");
  
  // Captura todos os botões de fechar
  const closeButtons = document.querySelectorAll("[id$='button-close']");
  
  // Função para ocultar todas as divs
  function hideAllDivs() {
    const divs = document.querySelectorAll("#consultas, #atendimento, #lista_de_medicos, #paciente, #historico");
    divs.forEach(function (div) {
      div.style.display = "none";
    });
  }

  // Função para exibir a div correspondente ao link clicado
  function showDiv(targetId) {
    hideAllDivs();
    const targetDiv = document.querySelector(targetId);
    if (targetDiv) {
      targetDiv.style.display = "block";
    }
  }

  // Adiciona o evento de clique aos links do sumário
  links.forEach(function (link) {
    link.addEventListener("click", function (e) {
      e.preventDefault();
      const targetId = this.getAttribute("href");
      showDiv(targetId);
    });
  });

  // Adiciona o evento de clique para os botões de fechar
  closeButtons.forEach(function (button) {
    button.addEventListener("click", function () {
      hideAllDivs();
    });
  });
});

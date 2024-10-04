
  // Validação básica do CPF
const cpfInput = document.getElementById('cpfInput');
cpfInput.addEventListener('input', function() {
let cpf = this.value.replace(/[^0-9]/g, ''); // Remove caracteres não numéricos
cpf = cpf.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, '$1.$2.$3-$4'); // Formata o CPF

this.value = cpf;
});

// Outras validações podem ser adicionadas aqui


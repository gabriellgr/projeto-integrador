from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class PacienteManager(BaseUserManager):
    """
    Gerenciador de usuários personalizados para o modelo Paciente.
    """
    def create_user(self, cpf, password, **extra_fields):
        """
        Cria e salva um novo usuário.
        """
        if not cpf:
            raise ValueError(_('O CPF é obrigatório'))
        cpf = self.normalize_email(cpf)  # Use normalize_email para formatar o CPF (opcional)
        user = self.model(cpf=cpf, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, cpf, password, **extra_fields):
        """
        Cria e salva um novo superusuário.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superusuário precisa ter is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superusuário precisa ter is_superuser=True.'))

        return self.create_user(cpf, password, **extra_fields)

class Paciente(AbstractBaseUser, PermissionsMixin):
    """
    Modelo de usuário Paciente.
    """
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)  # Email pode ser opcional
    data_de_nascimento = models.DateField(
        default=timezone.now,
        help_text=f'eg. {str(timezone.now().date())}'
    )
    cpf = models.CharField(max_length=11, unique=True)
    password = models.CharField(max_length=128)

    # Adiciona os campos is_staff e is_superuser
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'cpf'  # Define o CPF como o campo de identificação principal
    REQUIRED_FIELDS = ['email', 'password']  # Email agora é opcional

    objects = PacienteManager()
    # ... (restante do código)

    def __str__(self):
        return self.nome

    # ... (restante do código) 

    # ... (restante do código)     
class Medicos(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    funcao = models.CharField(max_length=100)
    data_consulta = models.DateField(null=False)#deve ter ao menos uma data
    
    def __str__(self):
        return self.nome

    def __str__(self):
        return self.nome
    def save(self, *args, **kwargs):
        super(Medicos, self).save(*args, **kwargs)
    def delete(self, *args, **kwargs):
        super(Medicos, self).delete(*args, **kwargs)
    

#exemplo de uso:
'''

from seu_app.models import Medicos # Substitua 'seu_app' pelo nome do seu app

# Criar um novo objeto Medicos
novo_medico = Medicos(nome='Dr. John Doe', funcao='Cardiologista', data_consulta='2023-10-27')

# Salvar o objeto no banco de dados
novo_medico.save()

'''
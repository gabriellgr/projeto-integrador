from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.utils.timezone import timedelta
from django.core.validators import MinValueValidator, MaxValueValidator


class PacienteManager(BaseUserManager):
    """
    Gerenciador de usuários personalizados para o modelo Paciente.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Cria e salva um novo usuário.
        """
        if not email:
            raise ValueError(_('O endereço de email é obrigatório'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Cria e salva um novo superusuário.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superusuário precisa ter is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superusuário precisa ter is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)

class Paciente(AbstractBaseUser, PermissionsMixin):
    """
    Modelo de usuário Paciente.
    """
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    data_de_nascimento = models.DateField(
        default=timezone.now,
        help_text=f'eg. {str(timezone.now().date())}'
    )
    cpf = models.CharField(max_length=11, unique=True)
    password = models.CharField(max_length=128)

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['nome', 'password']

    objects = PacienteManager()
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='paciente_set',  # Nome exclusivo para o acessor inverso
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='paciente_set',  # Nome exclusivo para o acessor inverso
    )
    def __str__(self):
        return self.nome

    def has_perm(self, perm, obj=None):
        """
        Retorna se o usuário possui a permissão específica.
        """
        return self.is_superuser

    def has_module_perms(self, app_label):
        """
        Retorna se o usuário possui permissões para o aplicativo específico.
        """
        return self.is_superuser
    
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
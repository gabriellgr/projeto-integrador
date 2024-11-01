from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.
class MedicoManager(BaseUserManager):
    """
    Gerenciador de usuários personalizados para o modelo Medico.
    """
    def create_user(self, cpf, password, **extra_fields):
        """
        Cria e salva um novo médico.
        """
        if not cpf:
            raise ValueError(_('O CPF é obrigatório'))
        if not extra_fields.get('crm'):
            raise ValueError(_('O CRM é obrigatório'))
        cpf = self.normalize_email(cpf)  # Use normalize_email para formatar o CPF (opcional)
        user = self.model(cpf=cpf, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, cpf, password, **extra_fields):
        """
        Cria e salva um novo superusuário médico.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superusuário precisa ter is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superusuário precisa ter is_superuser=True.'))

        return self.create_user(cpf, password, **extra_fields)

class Medico(AbstractBaseUser, PermissionsMixin):
    """
    Modelo de usuário Medico.
    """
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)  # Email pode ser opcional
    data_de_nascimento = models.DateField(
                                          
        default=timezone.now,
        help_text=f'eg. {str(timezone.now().date())}'
    )
    cpf = models.CharField(max_length=11, unique=True, null=False, blank=True)
    crm = models.CharField(max_length=20, unique=True)  # Número de registro médico
    especialidade = models.CharField(max_length=100, blank=True, null=True)  # Campo para especialidade médica
    password = models.CharField(max_length=128)

    # Adiciona os campos is_staff e is_superuser
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'cpf'  # Define o CPF como o campo de identificação principal
    REQUIRED_FIELDS = ['email', 'crm', 'password']  # CRM e email são obrigatórios

    objects = MedicoManager()

    # Corrige o problema de nomes conflitantes com related_name
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='medico_set',  # Nome exclusivo para o relacionamento do Medico
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='medico_permissions_set',  # Nome exclusivo para o relacionamento do Medico
        blank=True
    )

    def __str__(self):
        return self.nome

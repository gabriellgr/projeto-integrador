from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from medicos.models import Medico

@admin.register(Medico)
class MedicoAdmin(UserAdmin):
    """
    Customização do Django Admin para o modelo Medico.
    """
    list_display = ('cpf', 'nome', 'email', 'crm', 'especialidade', 'is_staff', 'is_superuser')
    search_fields = ('cpf', 'nome', 'email', 'crm')  # Permite buscar por CPF, nome, email ou CRM
    ordering = ('cpf',)
    fieldsets = (
        (None, {'fields': ('cpf', 'password')}),
        ('Informações Pessoais', {'fields': ('nome', 'email', 'crm', 'especialidade', 'data_de_nascimento')}),
        ('Permissões', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('cpf', 'nome', 'email', 'crm', 'especialidade', 'password1', 'password2', 'is_staff', 'is_superuser'),
        }),
    )
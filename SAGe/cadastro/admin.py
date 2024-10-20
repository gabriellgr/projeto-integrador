from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Paciente 

class PacienteAdmin(UserAdmin):
    list_display = ('cpf', 'nome','password','email', 'data_de_nascimento', 'is_staff')
    list_filter = ('is_staff', 'is_superuser')
    search_fields = ('cpf', 'nome', 'email')
    ordering = ('cpf',) 

    fieldsets = (
        (None, {'fields': ('cpf', 'nome','email', 'data_de_nascimento')}),
        ('Permissões', {'fields': ('is_staff', 'is_superuser')}),
        ('Informações importantes', {'fields': ('password',)}),
    )

    add_fieldsets = (
        (None, {'fields': ('cpf', 'nome', 'email', 'data_de_nascimento')}),
    )

admin.site.register(Paciente, PacienteAdmin)
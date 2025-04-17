from django.contrib import admin
from .models import Usuario
from django.contrib.auth.admin import UserAdmin

class UsuarioAdmin(UserAdmin):
    fieldsets= UserAdmin.fieldsets + (
        ('Campos novos', {
            'fields': ('telefone', 'data_nascimento', 'foto_perfil')
        }),
    )

    add_fieldsets= UserAdmin.add_fieldsets + (
        ('Campos novos', {
            'fields': ('telefone', 'data_nascimento', 'foto_perfil')
        }),
    )

admin.site.register(Usuario, UsuarioAdmin)

# Register your models here.

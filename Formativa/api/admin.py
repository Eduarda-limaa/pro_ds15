from django.contrib import admin
from .models import Usuario, Disciplina, ReservaAmbiente
from django.contrib.auth.admin import UserAdmin


class UsuarioAdmin(UserAdmin):
    fieldsets= UserAdmin.fieldsets + (
        ('Novos campos', {'fields': ('categoria', 'ni', 'telefone')}),
    )
    add_fieldsets= UserAdmin.add_fieldsets + (
        (None, {'fields': ('categoria', 'ni', 'telefone')}),
    )

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Disciplina)
admin.site.register(ReservaAmbiente)
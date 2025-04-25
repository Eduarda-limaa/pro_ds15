from django.contrib import admin
from .models import Usuario, Produto
from django.contrib.auth.admin import UserAdmin

class UsuarioAdmin(UserAdmin):
    fieldsets= UserAdmin.fieldsets + (
        ('Novos campos', {'fields': ('categoria',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('categoria', )}),
    )

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Produto)
from django.contrib import admin
from .models import Sensores, Historico, Ambientes

admin.site.register(Sensores)
admin.site.register(Historico)
admin.site.register(Ambientes)


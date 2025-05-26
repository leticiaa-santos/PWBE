from django.contrib import admin
from .models import Sensores, Ambientes, Historico

admin.site.register(Sensores)
admin.site.register(Ambientes)
admin.site.register(Historico)

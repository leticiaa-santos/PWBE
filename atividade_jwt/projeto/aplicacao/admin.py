from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):

    # campos que serão mostrados quando exibir o usuário
    list_display = ('username', 'email', 'biografia', 'idade', 'telefone', 'endereco', 'escolaridade', 'quantidade_animal')

    # campos que serão necessários serem preenchidos, além dos que já estão pré-definidos
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('biografia', 'idade', 'telefone', 'endereco', 'escolaridade', 'quantidade_animal')}),
    )

    # adiciona outros campos além dos que já são padrão
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('biografia', 'idade', 'telefone', 'endereco', 'escolaridade', 'quantidade_animal')}),
    )

admin.site.register(Usuario, UsuarioAdmin)


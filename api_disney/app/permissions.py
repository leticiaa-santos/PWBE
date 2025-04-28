from rest_framework.permissions import BasePermission

class IsGestor(BasePermission): # para as permissoes personalizadas
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.colaborador == 'G' # o usuário precisa estar autenticado e precisa ser gestor
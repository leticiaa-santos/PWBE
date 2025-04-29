from rest_framework.permissions import BasePermission

class IsGestor(BasePermission): # para as permissoes personalizadas
    def has_permission(self, request, view): # permissão geral
        return request.user.is_authenticated and request.user.colaborador == 'G' # o usuário precisa estar autenticado e precisa ser gestor
    
class IsGestorOuDono(BasePermission):
    def has_object_permission(self, request, view, obj): # permissão para um objeto especifico (id)
        if request.user.colaborador == 'G':
            return True
        return obj.usuario == request.user # verifica se o objeto pertence a quem quer alterá-lo
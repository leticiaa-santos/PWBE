from rest_framework.permissions import BasePermission

class IsGestor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticaded and request.user.tipo == 'G' # permite que apenas o usuário autenticado, sendo gestor tenha as permissões
    
class IsProfessor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.tipo == 'P' # permite que apenas o usuário autenticado, sendo professor tenha as permissões
    
class IsDonoOuGestor(BasePermission):
    def has_object_permission(self, request, view, obj): # método para um objeto específico
        if request.user.tipo == 'G':
            return True
        return obj.professor == request.user
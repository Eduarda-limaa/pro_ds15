from rest_framework.permissions import BasePermission


class IsGestor(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.categoria == 'G':
            return True
        return False
    

class IsUsuario(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.categoria == 'P':
            return True
        return False
    
    
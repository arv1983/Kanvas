from rest_framework.permissions import BasePermission

class PermissionSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser

class PermissionStaff(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


# Estudante - terá ambos os campos is_staff e is_superuser com o valor False
# Facilitador - terá os campos is_staff == True e is_superuser == False
# Instrutor - terá ambos os campos is_staff e is_superuser com o valor True
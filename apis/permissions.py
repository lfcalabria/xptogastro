from rest_framework.permissions import BasePermission


class IsFinanceiro(BasePermission):
    def has_permission(self, request, view):
        authorized_group_name = 'Financeiro'
        return request.user.is_authenticated and request.user.groups.filter(name=authorized_group_name).exists()


class IsProfessor(BasePermission):
    def has_permission(self, request, view):
        authorized_group_name = 'Professor'
        return request.user.is_authenticated and request.user.groups.filter(name=authorized_group_name).exists()


class IsPedagogico(BasePermission):
    def has_permission(self, request, view):
        authorized_group_name = 'Depto Pedagogico'
        return request.user.is_authenticated and request.user.groups.filter(name=authorized_group_name).exists()


class DenySuperuser(BasePermission):
    def has_permission(self, request, view):
        # Negar permissão se o usuário for um superusuário
        return not request.user.is_superuser

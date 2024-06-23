from rest_framework.permissions import BasePermission


class IsFinanceiro(BasePermission):
    def has_permission(self, request, view):
        authorized_group_name = 'Financeiro'
        return request.user.is_authenticated and request.user.groups.filter(name=authorized_group_name).exists()


class IsProfessores(BasePermission):
    def has_permission(self, request, view):
        authorized_group_name = 'Professores'
        print((request.user.groups.name))
        return request.user.is_authenticated and request.user.groups.filter(name=authorized_group_name).exists()


class IsPedagogico(BasePermission):
    def has_permission(self, request, view):
        authorized_group_name = 'Depto Pedagogigo'
        return request.user.is_authenticated and request.user.groups.filter(name=authorized_group_name).exists()

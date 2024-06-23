from django.utils.datetime_safe import date
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from apis.funcoes import movimentaproduto
from apis.serializers import *


class AulaViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = Aula.objects.filter(ativo=True)
    serializer_class = AulaSerializer

    def perform_create(self, serializer):
        data_aula = serializer.validated_data.get('data')
        if data_aula and data_aula < date.today():
            raise ValidationError("A data da aula não pode estar no passado para criação.")
        serializer.save(usuario=self.request.user)

    def perform_update(self, serializer):
        serializer.validated_data['usuario'] = str(self.request.user)
        serializer.save()


class AulaReceitaViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = AulaReceita.objects.filter(ativo=True)
    serializer_class = AulaReceitaSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    def perform_update(self, serializer):
        serializer.validated_data['usuario'] = str(self.request.user)
        serializer.save()


class DisciplinaViewSet(viewsets.ModelViewSet):
    """
    Cadastro de Disciplinas
    """
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = Disciplina.objects.filter(ativo=True)
    serializer_class = DisciplinaSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    def perform_update(self, serializer):
        serializer.validated_data['usuario'] = str(self.request.user)
        serializer.save()


class FornecedorViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = Fornecedor.objects.filter(ativo=True)
    serializer_class = FornecedorSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    def perform_update(self, serializer):
        serializer.validated_data['usuario'] = str(self.request.user)
        serializer.save()


class ItemNotaFiscalViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = ItemNotaFiscal.objects.filter(ativo=True)
    serializer_class = ItemNotaFicalSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    def perform_update(self, serializer):
        serializer.validated_data['usuario'] = str(self.request.user)
        serializer.save()


class LaboratorioViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = Laboratorio.objects.filter(ativo=True)
    serializer_class = LaboratorioSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    def perform_update(self, serializer):
        serializer.validated_data['usuario'] = str(self.request.user)
        serializer.save()


class MovimentoViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = Movimento.objects.filter(ativo=True)
    serializer_class = MovimentoSerializer

    def create(self, request, *args, **kwargs):
        tipo = request.data['tipo']
        if tipo.upper() == 'S':
            return Response('Saída de prodúto só por confirmação de aula', status=status.HTTP_400_BAD_REQUEST)
        if tipo.upper() == 'E':
            return Response('Entrada de prodúto deve ser feita pela nota fiscal', status=status.HTTP_400_BAD_REQUEST)
        if tipo.upper() == 'D':
            return Response('Devolução de prodúto deve ser feita pela devolução de produto', status=status.HTTP_400_BAD_REQUEST)
        if tipo.upper() == 'A':
            return Response('Movimentação de auditoria deve ser feita pela auditoria', status=status.HTTP_400_BAD_REQUEST)
        return Response('Tipo inválido', status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        tipo = request.data['tipo']
        if tipo.upper() == 'S':
            return Response('Saída de prodúto só por confirmação de aula', status=status.HTTP_400_BAD_REQUEST)
        if tipo.upper() == 'E':
            return Response('Entrada de prodúto deve ser feita pela nota fiscal', status=status.HTTP_400_BAD_REQUEST)
        if tipo.upper() == 'D':
            return Response('Devolução de prodúto deve ser feita pela devolução de produto',
                            status=status.HTTP_400_BAD_REQUEST)
        if tipo.upper() == 'A':
            return Response('Movimentação de auditoria deve ser feita pela auditoria',
                            status=status.HTTP_400_BAD_REQUEST)
        return Response('Tipo inválido', status=status.HTTP_400_BAD_REQUEST)


class NotaFiscalViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions, )
    queryset = NotaFiscal.objects.filter(ativo=True)
    serializer_class = NotaFiscalSerializer

    def create(self, request, *args, **kwargs):
         return Response('Deve ser utilizado a funcionalidade de entrada de nota fiscal', status=status.HTTP_400_BAD_REQUEST)

    def creupdateate(self, request, *args, **kwargs):
        return Response('Nota Fiscal não pode ser alterada',
                        status=status.HTTP_400_BAD_REQUEST)


class PrecoViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = Preco.objects.filter(ativo=True)
    serializer_class = PrecoSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    def perform_update(self, serializer):
        serializer.validated_data['usuario'] = str(self.request.user)
        serializer.save()


class ProdutoViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = Produto.objects.filter(quantidade__gt=0) | Produto.objects.filter(ativo=True)
    serializer_class = ProdutoSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    def perform_update(self, serializer):
        serializer.validated_data['usuario'] = str(self.request.user)
        serializer.save()


class ProfessorViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = Professor.objects.filter(ativo=True)
    serializer_class = ProfessorSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    def perform_update(self, serializer):
        serializer.validated_data['usuario'] = str(self.request.user)
        serializer.save()


class ReceitaViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = Receita.objects.filter(ativo=True)
    serializer_class = ReceitaSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    def perform_update(self, serializer):
        serializer.validated_data['usuario'] = str(self.request.user)
        serializer.save()


class ReceitaProdutoViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = ReceitaProduto.objects.filter(ativo=True)
    serializer_class = ReceitaProdutoSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    def perform_update(self, serializer):
        serializer.validated_data['usuario'] = str(self.request.user)
        serializer.save()


class TipoCulinariaViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = TipoCulinaria.objects.filter(ativo=True)
    serializer_class = TipoCulinariaSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    def perform_update(self, serializer):
        serializer.validated_data['usuario'] = str(self.request.user)
        serializer.save()


class UnidadeMedidaViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = UnidadeMedida.objects.filter(ativo=True)
    serializer_class = UnidadeMedidaSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    def perform_update(self, serializer):
        serializer.validated_data['usuario'] = str(self.request.user)
        serializer.save()

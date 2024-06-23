import pandas as pd
from django.shortcuts import render
from django.utils.datetime_safe import date
from django_pandas.io import read_frame
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apis.funcoes import precomedio
from apis.permissions import IsFinanceiro
from apis.serializers import *


def index(request):
    context = {"dados": 'Apis para o sistema de Controle de Produtos paras as aulas de Gastronomia'}
    return render(request, 'index.html', context)


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


class CustoDiarioApiView(APIView):
    permission_classes = (IsFinanceiro,)
    """
    Custo por dia de aula prática
    """

    def get(self, request):
        aulas = Aula.objects.all()
        df_aula = read_frame(aulas)
        aulas_receita = AulaReceita.objects.filter(aula__in=aulas, ativo=True)
        df_aulas_receita = read_frame(aulas_receita)
        df_aulas_receita['id_aula'] = aulas_receita.values_list('aula_id', flat=True)
        df_aulas_receita['id_receita'] = aulas_receita.values_list('receita_id', flat=True)
        df_custo = pd.merge(df_aula, df_aulas_receita, left_on=['id'],
                            right_on=['id_aula'], how='left')
        colunas = ['data', 'qtd_receita', 'id_receita']
        df_custo = df_custo[colunas]
        receitas_ingrediente = ReceitaProduto.objects.all()
        df_receitas_ingrediente = read_frame(receitas_ingrediente)
        df_receitas_ingrediente['id_produto'] = receitas_ingrediente.values_list('produto_id', flat=True)
        df_receitas_ingrediente['id_receita'] = receitas_ingrediente.values_list('receita_id', flat=True)
        df_custo = pd.merge(df_custo, df_receitas_ingrediente, left_on=['id_receita'],
                            right_on=['id_receita'], how='left')
        df_custo['qtd'] = df_custo['qtd_receita'] * df_custo['quantidade']
        colunas = ['data', 'qtd', 'id_produto']
        df_custo = df_custo[colunas]
        df_custo = df_custo.groupby(['data', 'id_produto'])['qtd'].aggregate(['sum'])
        df_custo = df_custo.reset_index()
        precos = Preco.objects.all()
        df_precos = precomedio(precos)
        df_custo = pd.merge(df_custo, df_precos, left_on=['id_produto'],
                            right_on=['id_prod'], how='left')
        df_custo['sum'] = df_custo['sum'].astype(float)
        df_custo['mean'] = df_custo['mean'].astype(float)
        df_custo['custo'] = df_custo['sum'] * df_custo['mean']
        df_custo = df_custo.groupby(['data'])['custo'].aggregate(['sum'])
        df_custo = df_custo.reset_index()
        df_custo['sum'] = round(df_custo['sum'], 2)
        df_custo.columns = ['data', 'valor']
        serializer = CustoDiarioSerializer(df_custo.to_dict(orient='records'), many=True)
        return Response(serializer.data)

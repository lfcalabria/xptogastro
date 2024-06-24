from datetime import timedelta

from dateutil.parser import parse
from django.db import transaction
from django.shortcuts import render
from django.utils.datetime_safe import date
from rest_framework import viewsets, permissions, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from apis.funcoes import *
from apis.permissions import *
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


class PosicaoEstoqueApiView(APIView):
    permission_classes = (IsFinanceiro,)
    """
    Posição do Estque
    """
    def get(self, request):
        df_estoque = posicaoestoque()
        colunas = ['nome', 'unidade', 'quantidade', 'preco_medio', 'total']
        df_estoque = df_estoque[colunas]
        serializer = PosicaoEstoqueSerializer(df_estoque.to_dict(orient='records'), many=True)
        return Response(serializer.data)


class NecessidadeCompraApiView(APIView):
    permission_classes = (IsFinanceiro, )

    def get(self, request, format=None):
        data = request.query_params.get('data')
        confirmada = request.query_params.get('data')
        hoje = date.today()
        if data is None:
            data = hoje + timedelta(30)
        else:
            try:
                data = parse(data, dayfirst=True).date()
                if data < hoje:
                    return Response("Data não pode ser anterior a data atual", status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response("Data inválida", status=status.HTTP_400_BAD_REQUEST)
        if confirmada == None:
            confirmada = 'N'
        if confirmada.upper() == 'S':
            aulas = Aula.objects.filter(data__range=(hoje, data), confirmada=True)
        elif confirmada.upper() == 'N':
            aulas = Aula.objects.filter(data__range=(hoje, data), confirmada=False)
        else:
            return Response('confirmada deve ser S ou N', status=status.HTTP_400_BAD_REQUEST)
        df_aulas = read_frame(aulas)
        df_aulas_produtos = pd.DataFrame()
        for dado in df_aulas.itertuples():
            df_aula_produtos = produtosaula(dado.id)
            df_aulas_produtos = pd.concat([df_aulas_produtos, df_aula_produtos])
        colunas = ['id_produto', 'qtd_ingrediente']
        df_aulas_produtos = df_aulas_produtos[colunas]
        df_aulas_produtos = df_aulas_produtos.groupby(['id_produto'])['qtd_ingrediente'].aggregate(['sum'])
        df_aulas_produtos = df_aulas_produtos.reset_index()
        df_estoque = posicaoestoque(list(df_aulas_produtos.id_produto))
        df_estoque = pd.merge(df_estoque, df_aulas_produtos, left_on=['id'],
                              right_on=['id_produto'], how='left')
        df_estoque.fillna(0, inplace=True)
        df_estoque['necessidade'] = df_estoque['quantidade'] - df_estoque['sum']
        df_estoque['custo'] = df_estoque['necessidade'] * df_estoque['preco_medio']
        df_necessidade = df_estoque.query('necessidade < 0')
        df_necessidade['necessidade'] = df_necessidade['necessidade'] * -1
        df_necessidade['custo'] = df_necessidade['custo'] * -1
        colunas = ['nome', 'unidade', 'necessidade', 'custo']
        df_necessidade = df_necessidade[colunas]
        df_necessidade.columns = ['produto', 'unidade', 'quantidade', 'custo']
        serializer = NecessidadeCompraSerializer(df_necessidade.to_dict(orient='records'), many=True)
        return Response(serializer.data)


class DetalhesAulaApiView(generics.RetrieveAPIView):
    permission_classes = (IsProfessor | IsPedagogico, )
    serializer_class = AulaSerializer
    queryset = Aula.objects.select_related(
            'disciplina',
            'professor',
            'laboratorio',
        )

    def get(self, request, *args, **kwargs):
        aula = self.get_object()

        # ************************************
        # Informações da aula
        # ************************************
        dados = aula.__dict__
        df_aula = pd.DataFrame([dados])
        df_aula['professor'] = aula.professor
        df_aula['disciplina'] = aula.disciplina
        df_aula['laboratorio'] = aula.laboratorio
        colunas = ['id', 'data', 'turno', 'qtd_aluno', 'confirmada', 'professor',
                   'disciplina', 'laboratorio']
        df_aula = df_aula[colunas]
        del dados
        df_receitas = receitasaula(aula.id)
        df_produto = produtosaula(aula.id)
        colunas = ['ingrediente', 'unidade', 'qtd_ingrediente', 'custo']
        df_produto = df_produto[colunas]
        colunas = ['receita', 'tipoculinaria', 'qtd_receita']
        df_receitas = df_receitas[colunas]
        dict_receita = df_receitas.to_dict(orient='records')
        dict_produto = df_produto.to_dict(orient='records')
        item_receita = ReceitaItemSerializer(dict_receita, many=True)
        item_produto = ProdutoItemSerializer(dict_produto, many=True)
        detalhe = df_aula.to_dict(orient='records')
        detalhe[0]['receitas'] = item_receita.data
        detalhe[0]['produtos'] = item_produto.data
        serializer = DetalheAulaSerializer(detalhe[0])
        return Response(serializer.data)


class ConfirmaAulaApiView(generics.UpdateAPIView):
    queryset = Aula.objects.all()
    serializer_class = AulaSerializer

    def put(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def perform_update(self, serializer):
        serializer.validated_data['usuario'] = self.request.user.id
        serializer.save()

    @transaction.atomic
    def partial_update(self, request, *args, **kwargs):
        aula = self.get_object()
        if aula.confirmada:
            return Response("Aula já confirmada", status=status.HTTP_400_BAD_REQUEST)
        produtos = produtosaula(aula.id)
        for dado in produtos.itertuples():
            movimento = movimentaproduto(dado.id_produto, 'S', dado.qtd_ingrediente, self.request.user.id)
            movimento_dict = {"produto": dado.id_produto, "tipo": "S", "quantidade": dado.qtd_ingrediente}
            movimento_dict['usuario'] = self.request.user.id
            movimento_serializer = MovimentoSerializer(data=movimento_dict)
            if movimento_serializer.is_valid(raise_exception=True):
               movimento_serializer.save()
        aula.confirmada = True
        aula.usuario = self.request.user.id
        aula.save()
        return Response("Aula confirmada com sucesso", status=status.HTTP_200_OK)


from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register('receitasingrediente', ReceitaProdutoViewSet)
router.register('tiposculinaria', TipoCulinariaViewSet)
router.register('receitas', ReceitaViewSet)
router.register('unidadesmedida', UnidadeMedidaViewSet)
router.register('produtos', ProdutoViewSet)
router.register('precos', PrecoViewSet)
router.register('professores', ProfessorViewSet)
router.register('disciplinas', DisciplinaViewSet)
router.register('fornecedores', FornecedorViewSet)
router.register('laboratorios', LaboratorioViewSet)
router.register('receitasaula', AulaReceitaViewSet)
router.register('aulas', AulaViewSet)
router.register('movimentos', MovimentoViewSet)
router.register('notasfiscais', NotaFiscalViewSet)
router.register('itensnotasfiscais', ItemNotaFiscalViewSet)

urlpatterns = [
    path("", index),
    path('custodiario/', CustoDiarioApiView.as_view(), name='custodiario'),
    path('posicaoestoque/', PosicaoEstoqueApiView.as_view(), name='posicaoestoque'),
    path('necessidadecompra/', NecessidadeCompraApiView.as_view(), name='necessidadecompra'),
    path('detalheaula/<int:pk>/', DetalhesAulaApiView.as_view(), name='detalheaula'),
    path('confirmaaula/<int:pk>/', ConfirmaAulaApiView.as_view(), name='confirmaaula'),
    path('cancelaaula/<int:pk>/', CancelaAulaApiView.as_view(), name='cancelaaula'),
]
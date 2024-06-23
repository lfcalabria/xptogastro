from django.contrib import admin

from apis.models import *


@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = (
        'data',
        'turno',
        'disciplina',
        'professor',
        'laboratorio',
        'confirmada',
    )


@admin.register(AulaReceita)
class AulaReceitaAdmin(admin.ModelAdmin):
    list_display = (
        'aula',
        'receita',
    )


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
    )


@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
    )


@admin.register(ItemNotaFiscal)
class ItemNotaFiscalAdmin(admin.ModelAdmin):
    list_display = (
        'notafiscal',
        'produto',
    )


@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'localizacao',
    )


@admin.register(Movimento)
class MovimentoAdmin(admin.ModelAdmin):
    list_display = (
        'produto',
        'tipo',
        'quantidade',
    )


@admin.register(NotaFiscal)
class NotaFiscalAdmin(admin.ModelAdmin):
    list_display = (
        'data_emissao',
        'numero',
        'fornecedor',
    )


@admin.register(Preco)
class PrecoAdmin(admin.ModelAdmin):
    list_display = (
        'produto',
        'data_cotacao',
        'valor',
    )


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'quantidade',
        'unidade',
    )


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
    )


@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'tipo',
    )


@admin.register(ReceitaProduto)
class ReceitaProdutoAdmin(admin.ModelAdmin):
    list_display = (
        'receita',
        'produto',
        'quantidade',
    )


@admin.register(TipoCulinaria)
class TipoCulinariaAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
    )


@admin.register(UnidadeMedida)
class UnidadeMedidaAdmin(admin.ModelAdmin):
    list_display = (
        'sigla',
        'descricao',
    )

from django.db import models

from apis.validators import *


class Base(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True, db_comment='Momento da criação do dado')
    data_ateracao = models.DateTimeField(auto_now=True, db_comment='momento da atualização do dado')
    ativo = models.BooleanField(default=True, db_comment='Indicador se o dado ainda está ativo')
    usuario = models.CharField(max_length=50, null=False, blank=False, editable=False)

    class Meta:
        abstract = True


class Aula(Base):
    TURNO_CHOICE = (
        ('M', 'Manhã'),
        ('T', 'Tarde'),
        ('V', 'Vespertino'),
        ('N', 'Noite'),
        ('I', 'Integral'),
    )
    data = models.DateField(blank=False, null=False, db_comment='Data da aula')
    turno = models.CharField(max_length=1, blank=False, null=False,
                             db_comment='Turno da aula', choices=TURNO_CHOICE)
    qtd_aluno = models.IntegerField(blank=False, null=False,validators=[validate_not_zero],
                                    db_comment='Número de alunos previsto')
    confirmada = models.BooleanField(blank=False, null=False, default=False,
                                     db_comment='Indicador se aula confirmada')
    ministrada = models.BooleanField(blank=False, null=False, default=False,
                                     db_comment='Indicador se aula ministrada')
    disciplina = models.ForeignKey('Disciplina', on_delete=models.RESTRICT,
                                   db_comment='Ligação com a tabela de disciplina')
    professor = models.ForeignKey('Professor', on_delete=models.RESTRICT,
                                  db_comment='Ligação com a tabela de professor')
    laboratorio = models.ForeignKey('Laboratorio', on_delete=models.RESTRICT,
                                    db_comment='Ligação com a tabela de laboratorio')
    receitas = models.ManyToManyField('Receita', through='AulaReceita')

    def __str__(self):
        return "Disciplina: " + str(self.disciplina) + ", Data: " + str(self.data) + ", Turno: " + str(self.turno)

    class Meta:
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'
        unique_together = ('data', 'turno', 'professor')
        indexes = (
            models.Index(fields=('disciplina',)),
            models.Index(fields=('professor',)),
            models.Index(fields=('laboratorio',)),
        )
        db_table = 'tbaula'
        ordering = ['data', 'turno', 'disciplina']
        db_table_comment = 'Tabela para armazenar o registro das aulas'


class AulaReceita(Base):
    aula = models.ForeignKey('Aula', on_delete=models.RESTRICT,
                             db_comment='Ligação com a tabela de aula')
    receita = models.ForeignKey('Receita', on_delete=models.RESTRICT,
                                db_comment='Ligação com a tabela de receita')

    qtd_receita = models.IntegerField(blank=False, null=False,validators=[validate_not_zero],
                                      db_comment='Quantidade de receitas previstas para a aula')

    def __str__(self):
        return "Receita: " + str(self.receita) + ", Aula: " + str(self.aula)

    class Meta:
        verbose_name = 'Receita da Aula'
        verbose_name_plural = 'Receitas das Aulas'
        unique_together = ('aula', 'receita')
        indexes = (
            models.Index(fields=('aula',)),
            models.Index(fields=('receita',)),
        )
        db_table = 'tbaulareceita'
        db_table_comment = 'Tabela associativa entre aula e receita'


class Disciplina(Base):
    nome = models.CharField(max_length=100, blank=False, unique=True, null=False,
                            db_comment='Nome da disciplina')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'
        indexes = (
            models.Index(fields=('nome',)),
        )
        db_table = 'tbdisciplina'
        ordering = ['nome']
        db_table_comment = 'Tabelas com as disciplinas que têm aulas práticas do curso de gastronomia'


class Fornecedor(Base):
    nome = models.CharField(max_length=100, blank=False, unique=True, null=False,
                            db_comment='Nome do fornecedor')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        indexes = (
            models.Index(fields=('nome',)),
        )
        db_table = 'tbfornecedor'
        ordering = ['nome']
        db_table_comment = 'Tabela com os fornecedores de insumo para as aulas práticas do curso de gastronomia'


class ItemNotaFiscal(Base):
    notafiscal = models.ForeignKey('NotaFiscal', on_delete=models.RESTRICT,
                                   db_comment='ligacao com a tabela de nota fiscal')
    produto = models.ForeignKey('Produto', on_delete=models.RESTRICT,
                                   db_comment='ligacao com a tabela de produtos')
    preco_unitario = models.DecimalField(max_digits=9, decimal_places=2,
                                db_comment='preço unitário do produto',
                                blank=False, null=False
                                )
    quantidade = models.DecimalField(max_digits=11, decimal_places=5,
                                     db_comment='Quantidade comprada',
                                     blank=False, null=False
                                     )

    def __str__(self):
        return "Nota Fiscal: " + str(self.notafiscal) + ", Produto: " + str(self.produto)

    class Meta:
        verbose_name = 'Item da Nota Fiscal'
        verbose_name_plural = 'Itens da Notas Fiscais'
        indexes = (
            models.Index(fields=('notafiscal',)),
            models.Index(fields=('produto',)),
        )
        db_table = 'tbitemnotafiscal'
        ordering = ['notafiscal', 'produto']
        unique_together = ['notafiscal', 'produto']
        db_table_comment = 'Tabela associativa entre nota fiscal e produto'


class Laboratorio(Base):
    nome = models.CharField(max_length=100, blank=False, unique=True, null=False,
                            db_comment='Nome do laboratório')
    localizacao = models.CharField(max_length=100, blank=False, unique=True, null=False,
                                   db_comment='Localização do laboratório')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Laboratório'
        verbose_name_plural = 'Laboratórios'
        indexes = (
            models.Index(fields=('nome',)),
        )
        db_table = 'tblaboratorio'
        ordering = ['nome']
        db_table_comment = 'Laboratórios disponíveis para as aulas práticas do curso de gastronomia'


class Movimento(Base):
    TIPO_CHOICE = (
        ('E', 'Entrada'),
        ('S', 'Saída'),
        ('A', 'Ajuste de auditoria'),
        ('D', 'Devolução'),
    )
    produto = models.ForeignKey('Produto', on_delete=models.RESTRICT,
                                db_comment='Ligação com a tabela de produto')
    tipo = models.CharField(max_length=1, blank=False, null=False,
                            db_comment='Tipo do movimento', choices=TIPO_CHOICE)
    quantidade = models.DecimalField(blank=False, null=False, max_digits=9, decimal_places=5,
                                     db_comment='Quantidade movimentada')

    def __str__(self):
        return str(self.tipo) + ", Quantidade: " + str(self.quantidade) + ", Produto: " + str(self.produto)

    class Meta:
        verbose_name = 'Movimento'
        verbose_name_plural = 'Movimentos'
        indexes = (
            models.Index(fields=('produto',)),
        )
        db_table = 'tbmovimento'
        ordering = ['produto', 'tipo']
        db_table_comment = 'Tabela para registro da movimentação de entrada e saída dos produtos '


class NotaFiscal(Base):
    data_emissao = models.DateField(blank=False, null=False, validators=[validate_not_in_future],
                                    db_comment='Data de emissão da nota fiscal')
    numero = models.CharField(blank=False, null=False,max_length=50,
                              db_comment='Número da nota fiscal')
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.RESTRICT,
                                   db_comment='ligacao com a tabela de fornecedor')

    def __str__(self):
        return "Nota Fiscal: " + str(self.id)

    class Meta:
        verbose_name = 'Nota Fiscal'
        verbose_name_plural = 'Notas Fiscais'
        indexes = (
            models.Index(fields=('fornecedor',)),
        )
        unique_together = ['fornecedor', 'numero']
        db_table = 'tbnotafiscal'
        ordering = ['data_emissao']
        db_table_comment = 'Registro de notas fiscais de compra para as aulas práticas do curso de gastronomia'


class Preco(Base):
    produto = models.ForeignKey('Produto', on_delete=models.RESTRICT,
                                db_comment='ligação com tabela de produto')
    data_cotacao = models.DateField(blank=False, null=False,validators=[validate_not_in_future],
                                    db_comment='Data Cotação')
    valor = models.DecimalField(max_digits=9, decimal_places=2, blank=False, null=False,
                                validators=[validate_not_zero],
                                db_comment='Valor cotado por unidade de medida',
                                )

    def __str__(self):
        return "Produto: " + str(self.produto) + ", Data: " + str(self.data_cotacao) + ', Valor R$' + str(self.valor)

    class Meta:
        verbose_name = 'Preço'
        verbose_name_plural = 'Preços'
        indexes = (
            models.Index(fields=('produto',)),
        )
        db_table = 'tbpreco'
        ordering = ['produto']
        db_table_comment = 'Tabela para armazenar o histórico de cotações de preços dos produtos'


class Produto(Base):
    nome = models.CharField(max_length=100, blank=False, unique=True, null=False,
                            db_comment='Nome do produto')
    quantidade = models.DecimalField(default=0, max_digits=11, decimal_places=5,
                                     db_comment='Quantidade disponível')
    unidade = models.ForeignKey('UnidadeMedida', on_delete=models.RESTRICT,
                                db_comment='ligação com tabela de unidade de medida')
    receitas = models.ManyToManyField('Receita', through='ReceitaProduto')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        indexes = (
            models.Index(fields=('nome',)),
            models.Index(fields=('unidade',)),
        )
        db_table = 'tbproduto'
        ordering = ['nome']
        db_table_comment = 'Tabela de produtos que são insumos para as aulas práticas do curso de gastronomia'


class Professor(Base):
    nome = models.CharField(max_length=100, blank=False, null=False,
                            db_comment='Nome do professor')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'
        indexes = (
            models.Index(fields=('nome',)),
        )
        db_table = 'tbprofessor'
        ordering = ['nome']
        db_table_comment = 'Professores das aulas práticas do curso de gastronomia'


class Receita(Base):
    nome = models.CharField(max_length=100, blank=False, unique=True, null=False,
                            db_comment='Nome do tipo de receita')
    tipo = models.ForeignKey('TipoCulinaria', on_delete=models.RESTRICT,
                             related_name='tipoculinara',
                             db_comment='ligacao com a tabela de tipo de culinaria')
    ingredientes = models.ManyToManyField('Produto', through='ReceitaProduto')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'
        unique_together = ('nome', 'tipo')
        indexes = (
            models.Index(fields=('nome',)),
            models.Index(fields=('tipo',)),
        )
        db_table = 'tbreceita'
        ordering = ['nome']
        db_table_comment = 'Receitas utilizadas nas aulas práticas do curso de gastronomia'


class ReceitaProduto(Base):
    receita = models.ForeignKey('Receita', on_delete=models.RESTRICT,
                                db_comment='ligação com a tabela de receita')
    produto = models.ForeignKey('Produto', on_delete=models.RESTRICT,
                                db_comment='ligação com a tabela de produto')
    quantidade = models.DecimalField(max_digits=11, decimal_places=5, validators=[validate_not_zero],
                                     db_comment='quantidade usada na receita por unidade de medida',
                                     )

    def __str__(self):
        return "Receita:" + str(self.receita) + ", Produto:" + str(self.produto)

    class Meta:
        verbose_name = 'Ingrediente da Receita'
        verbose_name_plural = 'Ingredientes da Receita'
        unique_together = ('receita', 'produto')
        indexes = (
            models.Index(fields=('receita',)),
            models.Index(fields=('produto',)),
        )
        db_table = 'tbreceitaproduto'
        db_table_comment = 'Tabela associativa entre receita e produto'


class TipoCulinaria(Base):
    nome = models.CharField(max_length=100, blank=False, unique=True, null=False,
                            db_comment='Nome do tipo de culinária')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Tipo de Culinária'
        verbose_name_plural = 'Tipos de Culinária'
        indexes = (
            models.Index(fields=('nome',)),
        )
        db_table = 'tbtipoculinaria'
        ordering = ['nome']
        db_table_comment = 'Tipos de culinária'


class UnidadeMedida(Base):
    sigla = models.CharField(max_length=5, blank=False, unique=True, null=False,
                             db_comment='Sigla da unidade de medida')
    descricao = models.CharField(max_length=100, blank=False, null=False,
                                 db_comment='Descrição da unidade de medida')

    def __str__(self):
        return str(self.sigla) + ' - ' + str(self.descricao)

    class Meta:
        verbose_name = 'Unidade de Medida'
        verbose_name_plural = 'Unidades de Medida'
        indexes = (
            models.Index(fields=('sigla',)),
        )
        db_table = 'tbunidademedida'
        ordering = ['sigla']
        db_table_comment = 'Unidade de medida dos produtos'

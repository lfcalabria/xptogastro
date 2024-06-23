from rest_framework import serializers

from apis.models import *


class AulaSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            validated_data['usuario'] = request.user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            validated_data['usuario'] = request.user
        return super().update(instance, validated_data)

    class Meta:
        model = Aula
        fields = '__all__'
        read_only_fields = ['confirmada', 'ministrada', 'ativo']


class AulaReceitaSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            validated_data['usuario'] = request.user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            validated_data['usuario'] = request.user
        return super().update(instance, validated_data)

    class Meta:
        model = AulaReceita
        fields = '__all__'
        read_only_fields = ['ativo']


class DisciplinaSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            validated_data['usuario'] = request.user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            validated_data['usuario'] = request.user
        return super().update(instance, validated_data)

    class Meta:
        model = Disciplina
        fields = '__all__'
        read_only_fields = ['ativo']


class FornecedorSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            validated_data['usuario'] = request.user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            validated_data['usuario'] = request.user
        return super().update(instance, validated_data)

    class Meta:
        model = Fornecedor
        fields = '__all__'
        read_only_fields = ['ativo']


class ItemNotaFicalSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            validated_data['usuario'] = request.user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            validated_data['usuario'] = request.user
        return super().update(instance, validated_data)

    class Meta:
        model = ItemNotaFiscal
        fields = '__all__'
        read_only_fields = ['ativo']


class LaboratorioSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            validated_data['usuario'] = request.user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            validated_data['usuario'] = request.user
        return super().update(instance, validated_data)

    class Meta:
        model = Laboratorio
        fields = '__all__'
        read_only_fields = ['ativo']


class MovimentoSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            validated_data['usuario'] = request.user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            validated_data['usuario'] = request.user
        return super().update(instance, validated_data)

    class Meta:
        model = Movimento
        fields = '__all__'
        read_only_fields = ['ativo']


class NotaFiscalSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            validated_data['usuario'] = request.user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            validated_data['usuario'] = request.user
        return super().update(instance, validated_data)

    class Meta:
        model = NotaFiscal
        fields = '__all__'
        read_only_fields = ['ativo']


class PrecoSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            validated_data['usuario'] = request.user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            validated_data['usuario'] = request.user
        return super().update(instance, validated_data)

    class Meta:
        model = Preco
        fields = '__all__'
        read_only_fields = ['ativo']


class ProdutoSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            validated_data['usuario'] = request.user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            validated_data['usuario'] = request.user
        return super().update(instance, validated_data)

    class Meta:
        model = Produto
        fields = '__all__'
        read_only_fields = ['ativo', 'quantidade']


class ProfessorSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            validated_data['usuario'] = request.user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            validated_data['usuario'] = request.user
        return super().update(instance, validated_data)

    class Meta:
        model = Professor
        fields = '__all__'
        read_only_fields = ['ativo']


class ReceitaSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            validated_data['usuario'] = request.user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            validated_data['usuario'] = request.user
        return super().update(instance, validated_data)

    class Meta:
        model = Receita
        fields = '__all__'
        read_only_fields = ['ativo']


class ReceitaProdutoSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            validated_data['usuario'] = request.user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            validated_data['usuario'] = request.user
        return super().update(instance, validated_data)

    class Meta:
        model = ReceitaProduto
        fields = '__all__'
        read_only_fields = ['ativo']


class TipoCulinariaSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            validated_data['usuario'] = request.user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            validated_data['usuario'] = request.user
        return super().update(instance, validated_data)

    class Meta:
        model = TipoCulinaria
        fields = '__all__'
        read_only_fields = ['ativo']


class UnidadeMedidaSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            validated_data['usuario'] = request.user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            validated_data['usuario'] = request.user
        return super().update(instance, validated_data)

    class Meta:
        model = UnidadeMedida
        fields = '__all__'
        read_only_fields = ['ativo']


class CustoDiarioSerializer(serializers.Serializer):
    data = serializers.DateField()
    valor = serializers.DecimalField(max_digits=11, decimal_places=2)


class PosicaoEstoqueSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=100)
    unidade = serializers.CharField(max_length=100)
    quantidade = serializers.DecimalField(max_digits=11, decimal_places=5)
    preco_medio = serializers.DecimalField(max_digits=11, decimal_places=2)
    total = serializers.DecimalField(max_digits=11, decimal_places=2)

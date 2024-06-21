from rest_framework import serializers
from financas.models import Usuario, Categoria, Credito, Debito

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'data_nascimento', 'email', 'senha', 'ativo', 'aceite_termo']

class UsuariosByIdSerializer(serializers.ModelSerializer):
    usuario = serializers.ReadOnlyField(source='usuario.nome')
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'data_nascimento', 'email', 'senha', 'ativo', 'aceite_termo']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id','titulo_categoria', 'descricao', 'tipo']

class CreditoSerializer(serializers.ModelSerializer):
    usuario = serializers.ReadOnlyField(source='usuario.nome')
    categoria = serializers.ReadOnlyField(source='categoria.titulo_categoria')
    class Meta:
        model = Credito
        fields = ['id', 'usuario', 'titulo_credito', 'data_entrada', 'valor', 'categoria', 'descricao']

class ExtratoCreditoUsuarioSerializer(serializers.ModelSerializer):
    categoria = serializers.ReadOnlyField(source='categoria.titulo_categoria')
    class Meta:
        model = Credito
        fields = ['titulo_credito', 'data_entrada', 'valor', 'categoria', 'descricao']

class DebitoSerializer(serializers.ModelSerializer):
    usuario = serializers.ReadOnlyField(source='usuario.nome')
    categoria = serializers.ReadOnlyField(source='categoria.titulo_categoria')
    class Meta:
        model = Debito
        fields = ['id', 'usuario', 'titulo_debito', 'data_saida', 'valor', 'categoria', 'descricao']

class ExtratoDebitoUsuarioSerializer(serializers.ModelSerializer):
    categoria = serializers.ReadOnlyField(source='categoria.titulo_categoria')
    class Meta:
        model = Debito
        fields = ['titulo_debito', 'data_saida', 'valor', 'categoria', 'descricao']
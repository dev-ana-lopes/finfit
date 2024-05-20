from rest_framework import serializers
from financas.models import Usuario, Categoria, Credito, Debito

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'data_nascimento', 'email']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id','titulo_categoria', 'descricao', 'tipo']

class CreditoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credito
        fields = ['id', 'usuario', 'titulo_credito', 'data_entrada', 'valor', 'categoria', 'descricao']

class DebitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debito
        fields = ['id', 'usuario', 'titulo_debito', 'data_saida', 'valor', 'categoria', 'descricao']

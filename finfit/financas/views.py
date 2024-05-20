from rest_framework import viewsets
from financas.models import Usuario, Categoria, Credito, Debito
from financas.serializers import UsuarioSerializer, CategoriaSerializer, CreditoSerializer, DebitoSerializer

#exibe todos os usuários
class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

#exibe todos as categorias
class CategoriasViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

#exibe todos os créditos
class CreditosViewSet(viewsets.ModelViewSet):
    queryset = Credito.objects.all()
    serializer_class = CreditoSerializer

class DebitosViewSet(viewsets.ModelViewSet):
    queryset = Debito.objects.all()
    serializer_class = DebitoSerializer



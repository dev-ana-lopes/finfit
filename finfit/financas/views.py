from rest_framework import viewsets, generics
from financas.models import Usuario, Categoria, Credito, Debito
from financas.serializers import *

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

#exibe os créditos por usuário
class ExtratoCreditoUsuario(generics.ListAPIView):
    def get_queryset(self):
        queryset = Credito.objects.filter(usuario_id=self.kwargs['pk'])
        return queryset
    serializer_class = ExtratoCreditoUsuarioSerializer

#exibe todos os débitos
class DebitosViewSet(viewsets.ModelViewSet):
    queryset = Debito.objects.all()
    serializer_class = DebitoSerializer

#exibe os débitos por usuário
class ExtratoDebitoUsuario(generics.ListAPIView):
    def get_queryset(self):
        queryset = Debito.objects.filter(usuario_id=self.kwargs['pk'])
        return queryset
    serializer_class = ExtratoDebitoUsuarioSerializer



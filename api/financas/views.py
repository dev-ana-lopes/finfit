from django.http import HttpRequest, HttpResponse
from rest_framework import viewsets, generics
from financas.models import Usuario, Categoria, Credito, Debito
from financas.serializers import *

#exibe todos os usuários - get, update, delete
class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

#exibe usuário por id - get, update, delete
class UsuariosById(generics.ListAPIView):
    def get_queryset(self):
        queryset = Usuario.objects.filter(usuario_id=self.kwargs['pk'])
        return queryset
    serializer_class = UsuariosByIdSerializer

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

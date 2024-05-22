from rest_framework import viewsets, generics
from financas.models import Usuario, Categoria, Credito, Debito
from financas.serializers import *
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

#exibe todos os usuários
class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

#exibe todos as categorias
class CategoriasViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

#exibe todos os créditos
class CreditosViewSet(viewsets.ModelViewSet):
    queryset = Credito.objects.all()
    serializer_class = CreditoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

#exibe os créditos por usuário
class ExtratoCreditoUsuario(generics.ListAPIView):
    def get_queryset(self):
        queryset = Credito.objects.filter(usuario_id=self.kwargs['pk'])
        return queryset
    serializer_class = ExtratoCreditoUsuarioSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

#exibe todos os débitos
class DebitosViewSet(viewsets.ModelViewSet):
    queryset = Debito.objects.all()
    serializer_class = DebitoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

#exibe os débitos por usuário
class ExtratoDebitoUsuario(generics.ListAPIView):
    def get_queryset(self):
        queryset = Debito.objects.filter(usuario_id=self.kwargs['pk'])
        return queryset
    serializer_class = ExtratoDebitoUsuarioSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


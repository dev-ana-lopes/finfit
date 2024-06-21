
from django.urls import path, include
from financas.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('usuarios', UsuariosViewSet, basename='Usuarios')
router.register('categorias', CategoriasViewSet, basename='Categorias')
router.register('creditos', CreditosViewSet, basename='Creditos')
router.register('debitos', DebitosViewSet, basename='Debitos')

urlpatterns = [
    path('', include(router.urls)),
    path('usuarios/<int:pk>/creditos/', ExtratoCreditoUsuario.as_view()),
    path('usuarios/<int:pk>/debitos/', ExtratoDebitoUsuario.as_view()),
    path('usuarios/<int:pk>/', UsuariosById.as_view()),
    
]
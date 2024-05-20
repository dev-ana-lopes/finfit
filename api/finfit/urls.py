from django.contrib import admin
from django.urls import path, include
from financas.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('usuario', UsuariosViewSet, basename='Usuario')
router.register('categoria', CategoriasViewSet, basename='Categoria')
router.register('credito', CreditosViewSet, basename='Credito')
router.register('debito', DebitosViewSet, basename='Debito')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('usuario/<int:pk>/credito/', ExtratoCreditoUsuario.as_view()),
    path('usuario/<int:pk>/debito/', ExtratoDebitoUsuario.as_view()),
    
]

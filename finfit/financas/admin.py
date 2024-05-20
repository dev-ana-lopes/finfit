from django.contrib import admin
from financas.models import Usuario, Categoria, Debito, Credito

class Usuarios(admin.ModelAdmin):
    list_display = ('id', 'nome', 'data_nascimento', 'email')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Usuario, Usuarios)

class Categorias(admin.ModelAdmin):
    list_display = ('id','titulo_categoria', 'descricao', 'tipo')
    list_display_links = ('id','titulo_categoria')
    search_fields = ('titulo_categoria',)
    list_per_page = 10

admin.site.register(Categoria, Categorias)

class Creditos(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'titulo_credito', 'data_entrada', 'valor', 'categoria', 'descricao')
    list_display_links = ('id', 'titulo_credito',)
    search_fields = ('titulo_credito',)
    list_per_page = 10

admin.site.register(Credito, Creditos)

class Debitos(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'titulo_debito', 'data_saida', 'valor', 'categoria', 'descricao')
    list_display_links = ('id', 'titulo_debito',)
    search_fields = ('titulo_debito',)
    list_per_page = 10

admin.site.register(Debito, Debitos)

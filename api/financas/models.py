from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    email = models.EmailField(unique=True, max_length=255)
    senha = models.CharField(max_length=20)
    ativo = models.BooleanField(default=True)
    aceite_termo = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    titulo_categoria = models.CharField(max_length=50)
    descricao = models.TextField(max_length=250, blank=True)
    TIPO = (
        ('C', 'Crédito'),
        ('D', 'Débito')
    )

    tipo = models.CharField(max_length=1, choices=TIPO, default='D')
    def __str__(self):
        return self.titulo_categoria
    
class Credito(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    titulo_credito = models.CharField(max_length=50)
    data_entrada = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(max_length=250, blank=True)
    
    def __str__(self):
        return self.titulo_credito
    
class Debito(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    titulo_debito = models.CharField(max_length=50)
    data_saida = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(max_length=250, blank=True)

    def __str__(self):
        return self.titulo_debito
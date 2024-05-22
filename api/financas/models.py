from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField()
    email = models.EmailField(unique=True)
    ativo = models.BooleanField(default=True, null=False)
    
    def __str__(self):
        return self.nome

class Categoria(models.Model):
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
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    titulo_credito = models.CharField(max_length=50)
    data_entrada = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(max_length=250, blank=True)
    
    def __str__(self):
        return self.titulo_credito
    
class Debito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    titulo_debito = models.CharField(max_length=50)
    data_saida = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(max_length=250, blank=True)

    def __str__(self):
        return self.titulo_debito
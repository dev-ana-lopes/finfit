from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField()
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.nome

class Categoria(models.Model):
    titulo_categoria = models.CharField(max_length=50)
    descricao = models.TextField(max_length=250)
    icone = models.ImageField()
    
    def __str__(self):
        return self.titulo_categoria
    
class Credito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo_credito = models.CharField(max_length=50)
    data_entrada = models.DateField()
    valor = models.FloatField()
    categoria = models.CharField()
    descricao = models.TextField()
    
    def __str__(self):
        return self.valor
    
class Debito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    titulo_debito = models.CharField(max_length=50)
    data_saida = models.DateField()
    valor = models.FloatField()
    descricao = models.TextField(max_length=250)

    def __str__(self):
        return self.valor
    
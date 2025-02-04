from django.db import models



# CRIAÇÃO DOS SCRIPTS DO BANCO DE DADOS

class Brand(models.Model): #classe Brand herda da classe Models
    id= models.AutoField(primary_key=True) #campo id com chave primaria e auto incremento
    name = models.CharField(max_length=200) #campo de texto com maximo de caracteres

    def __str__(self): #função para retornar o nome da marca
        return self.name #retorna o nome da marca

class Car(models.Model): #tabela Car herda da classe Models
    id = models.AutoField(primary_key=True) #campo id com chave primaria e auto incremento
    model = models.CharField(max_length=200, blank=True) #campo de texto com maximo de caracteres, vazio, nulo
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand') #campo de chave estrangeira, protegido, relacionado com a tabela Brand
    factory_year = models.IntegerField(blank=True, null=True) #campo de numero inteiro
    model_year = models.IntegerField(blank=True, null=True) #campo de numero inteiro
    value = models.FloatField(blank=True, null=True) #campo de numero flutuante

    def __str__(self): #função para retornar o modelo do carro
        return self.model #retorna o modelo do carro



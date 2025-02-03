from django.db import models

# CRIAÇÃO DOS SCRIPTS DO BANCO DE DADOS


class Car(models.Model): #tabela Car herda da classe Models
    id = models.AutoField(primary_key=True) #campo id com chave primaria e auto incremento
    model = models.CharField(max_length=200, blank=True) #campo de texto com maximo de caracteres, vazio, nulo
    brand = models.CharField(max_length=50) #campo texto com 50 caracteres
    factory_year = models.IntegerField(blank=True, null=True) #campo de numero inteiro
    model_year = models.IntegerField(blank=True, null=True) #campo de numero inteiro
    value = models.FloatField(blank=True, null=True) #campo de numero flutuante




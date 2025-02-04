from django.contrib import admin
from cars.models import Brand
from cars.models import Car


# Register your models here.

class CarAdmin(admin.ModelAdmin): #classe para customizar a exibição dos dados no admin
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value') #campos que serão exibidos na listagem
    search_fields = ('model','brand') #campo de busca por modelo e marca

admin.site.register(Car, CarAdmin) # registra o modelo Car no admin e aplica a customização da classe CarAdmin

class BrandAdmin(admin.ModelAdmin): #classe para customizar a exibição dos dados no admin
    list_display = ('name',) #campos que serão exibidos na listagem
    search_fields = ('name',) #campo de busca por nome

admin.site.register(Brand, BrandAdmin) # registra o modelo Brand no admin e aplica a customização da classe BrandAdmin
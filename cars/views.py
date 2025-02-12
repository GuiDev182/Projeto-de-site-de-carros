from django.shortcuts import render #importa a função render
from cars.models import Car

# Create your views here.
def cars_view(request): #cria a função cars_view
    cars = Car.objects.all() #busca todos os carros no banco de dados
    return render(request,
                  'cars.html',
                  {'cars': cars}
                  ) #retorna a página cars.html com a lista de carros

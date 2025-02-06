"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin    #importa a função admin
from django.urls import path    #importa a função path
from django.conf import settings    #importa as configurações do projeto
from django.conf.urls.static import static  #importa a função static

from cars.views import cars_view    #importa a função cars_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', cars_view)  #adiciona a url cars/ e a função cars_view
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #adiciona a url de media e o caminho da pasta de media


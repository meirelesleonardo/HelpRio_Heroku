# -*- encoding: utf-8 -*-

from django.urls import path, re_path
from . import views

app_name = 'ficha_imovel'

urlpatterns = [

    # The home page
    path('fichaImovel/criar', views.criar, name='criar'),  
    path('fichaImovel/lista', views.listar, name='lista'), 
    path('fichaImovel/laudo', views.laudo, name='laudo'),

]

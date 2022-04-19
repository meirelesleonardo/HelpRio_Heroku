# -*- encoding: utf-8 -*-

from django.urls import path, re_path
from users import views

app_name = 'users'

urlpatterns = [

    # The home page
    path('perfil', views.perfil, name='perfil'),   

]

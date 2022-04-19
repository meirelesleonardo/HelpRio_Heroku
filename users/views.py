from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url="/login/")
def perfil(request):
    context = {'segment': 'perfil'}

    html_template = loader.get_template('users/perfil.html')
    return HttpResponse(html_template.render(context, request))
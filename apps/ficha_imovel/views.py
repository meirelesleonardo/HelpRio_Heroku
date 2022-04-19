from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CriarLaudo


# Create your views here.
@login_required(login_url="/login/")
def listar(request):
    context = {'segment': 'ficha_imovel'}

    html_template = loader.get_template('ficha_imovel/lista.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def criar(request):
    form = CriarLaudo()
    context = {"form": form}

    # # html_template = loader.get_template('ficha_imovel/criar.html')
    # # return HttpResponse(html_template.render(context, request))
    # msg = None
    # success = False

    # if request.method == "POST":
                
    #     form = CriarLaudo(request.POST)
               
    #     if form.is_valid():
    #         novaFicha = form.save(commit=False)           
              
    #         #novoUsuario.save()
                       

    #         msg = 'Ficha criada com sucesso - <a href="/login/">login</a>.'
    #         success = True

    #         #return redirect("/login")

    #     else:
    #         msg = 'Form is not valid'
    # else:
    #     data = {'corretor':request.user}
    #     form = CriarLaudo()       
      

    return render(request, "ficha_imovel/criar.html", context=context)

@login_required(login_url="/login/")
def laudo(request):
    context = {'segment': 'ficha_imovel'}

    html_template = loader.get_template('ficha_imovel/laudo.html')
    return HttpResponse(html_template.render(context, request))
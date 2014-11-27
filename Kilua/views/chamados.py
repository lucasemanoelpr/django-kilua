from Kilua.forms import *
from django.contrib import messages
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from Kilua.models import Prioridade, Chamados
import datetime
from django.contrib.auth.models import User
from django.db.models import Q

@login_required
def add_chamado(request):


    if request.method == 'POST':

        form = ChamadosForm(request.POST)

        if form.is_valid():

            # Cadastro de prioridade

            call_form = ChamadosForm(data=request.POST)

            call_form.save()

            # Pega todos os ids de prioridade e ordena por ordem de entrada
            last_inserted = Prioridade.objects.order_by('-id')[0]
            priori = Prioridade.objects.get(id=last_inserted.id)

            # Cadastro de Chamados

            chamado = Chamados()
            chamado.id_prioridade = priori
            chamado.id_user = request.POST['id_user']
            chamado.data_inicio = datetime.datetime.now()

            chamado.save()


            return redirect('/kilua/controle/')

        else:
            messages.error(request, 'Ocorreu um erro ao cadastrar o Chamado. Tente novamente!')
            return redirect('/kilua/controle/add_chamado/')



    else:
        context = {}
        chamado_form = ChamadosForm()
        chamado_form.fields['id_user'].initial = request.user.id

        ## Permissao de usuario

        c = UserProfile.objects.filter(codigo_tpuser=3)
        var = []
        for i in c:
            var.append((User.objects.get(username=i.user)).username)
        context['form'] = chamado_form
        context['usuarios'] = var


        return render(request, 'add_chamado.html', context)

@login_required
def visualizar(request, chamado_id):


    context = {}

    if request.method == 'POST':
        form = ChamadosForm(request.POST)

        chamado = Chamados.objects.get(id_prioridade=chamado_id)
        chamado.data_termino = datetime.datetime.now()
        chamado.desc_solucao = request.POST['desc_solucao']
        chamado.save()
        return redirect('/kilua/controle/')



    else:

        # Essas linhas abaixo pegam os valores da tabela relacionada a chave estrangeira

        chama = Prioridade.objects.get(id=chamado_id)
        e = User.objects.get(id=chama.id_user)
        chamad = Chamados.objects.get(id_prioridade=chamado_id)
        form = AlterchamadosForm()
        context['chamados'] = chama
        context['usera'] = e
        context['chamad'] = chamad
        context['form'] = form

        # Permissao de usuario

        c = UserProfile.objects.filter(codigo_tpuser=3)
        var = []
        for i in c:
            var.append((User.objects.get(username=i.user)).username)

        context['usuarios'] = var

    return render(request, 'chamado.html', context)

#    return render_to_response('chamado.html', context)
@login_required
def historico(request):


    context = {}
    chama = []

    cham = Chamados.objects.filter(~Q(data_termino=None))

    if len(cham)>0:
        for z in cham:
            chama.append(z.id_prioridade)

        for x in chama:
            x.id_user = (User.objects.get(id=x.id_user))
            x.nivel = (Tipo_problema.objects.get(nome_tprob=x.id_tpproblema)).nivel_tprob

        context['chamados'] = chama

        # Permissao de usuario

        c = UserProfile.objects.filter(codigo_tpuser=3)
        var = []
        for i in c:
            var.append((User.objects.get(username=i.user)).username)

        context['usuarios'] = var



    return render(request, 'historico.html', context)

@login_required
def visualizar_historico(request, historico_id):


    context = {}
    chama = Prioridade.objects.get(id=historico_id)
    e = User.objects.get(id=chama.id_user)
    chamad = Chamados.objects.get(id_prioridade=historico_id)

    context['chamados'] = chama
    context['usera'] = e
    context['chamad'] = chamad

    # Permissao de usuario

    c = UserProfile.objects.filter(codigo_tpuser=3)
    var = []
    for i in c:
        var.append((User.objects.get(username=i.user)).username)

    context['usuarios'] = var


    return render(request, 'visualizar_historico.html', context)
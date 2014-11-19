from Kilua.forms import *
from django.contrib import messages
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from Kilua.models import Prioridade, Chamados
import datetime
from django.contrib.auth.models import User

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

        chamado_form = ChamadosForm()
        chamado_form.fields['id_user'].initial = request.user.id

        return render(request, 'add_chamado.html', {'form':chamado_form})

@login_required
def visualizar(request, chamado_id):


    context = {}


    if request.method == 'POST':
        pass

    else:

        chama = Prioridade.objects.get(id=chamado_id)
        # essa porra de linha abaixo pega os valores de tabela de uma chave estrangeira
        e = User.objects.get(id=chama.id_user)

        context['chamados'] = chama
        context['user'] = e

    return render_to_response('chamado.html', context)

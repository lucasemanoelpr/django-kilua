from Kilua.forms import *
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import datetime

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







            messages.success(request, 'Chamado salvo com sucesso!')
            return redirect('/kilua/controle/')

        else:
            messages.error(request, 'Ocorreu um erro ao cadastrar o Chamado. Tente novamente!')
            return redirect('/kilua/controle/add_chamado/')



    else:

        chamado_form = ChamadosForm()
        chamado_form.fields['id_user'].initial = request.user.id

        return render(request, 'add_chamado.html', {'form':chamado_form})
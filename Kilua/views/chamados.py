from Kilua.forms import *
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def add_chamado(request):


    if request.method == 'POST':

        form = ChamadosForm(request.POST)

        if form.is_valid():


            call_form = ChamadosForm(data=request.POST)

            call_form.save()



            messages.success(request, 'Chamado salvo com sucesso!')
            return redirect('/kilua/controle/')

        else:
            messages.error(request, 'Ocorreu um erro ao cadastrar o Chamado. Tente novamente!')
            return redirect('/kilua/controle/add_chamado/')



    else:

        chamado_form = ChamadosForm()

        return render(request, 'add_chamado.html', {'form':chamado_form})
from Kilua.forms import *
from django.contrib import messages
from django.shortcuts import render, redirect

def add_chamado(request):


    if request.method == 'POST':
        form = SetorForm(request.POST)

        if form.is_valid():
            setor = Setor()
            setor.nome_setor = request.POST['nome_setor']
            setor.localidade = request.POST['localidade']
            setor.telefone = request.POST['telefone']
            setor.save()

            messages.success(request, 'Chamado salvo com sucesso!')
            return redirect('/kilua/controle/')

        else:
            messages.error(request, 'Ocorreu um erro ao cadastrar o Chamado. Tente novamente!')
            return redirect('/kilua/controle/add_chamado/')



    else:

        form = ChamadosForm()

        return render(request, 'add_chamado.html', {'form':form})
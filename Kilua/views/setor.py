from Kilua.forms import *
from django.contrib import messages
from django.shortcuts import render, redirect

def add_setor(request):


    if request.method == 'POST':
        form = SetorForm(request.POST)

        if form.is_valid():
            setor = Setor()
            setor.nome_setor = request.POST['nome_setor']
            setor.localidade = request.POST['localidade']
            setor.telefone = request.POST['telefone']
            setor.save()

            messages.success(request, 'Setor salvo com sucesso!')
            return redirect('/kilua/controle/')

        else:
            messages.error(request, 'Ocorreu um erro ao cadastrar o Setor. Tente novamente!')
            return redirect('/controle/add_setor/')



    else:

        form = SetorForm()

    return render(request, 'add_setor.html', {'form':form})
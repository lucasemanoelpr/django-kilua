from Kilua.forms import *
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def add_setor(request):

    registered = False

    if request.method == 'POST':
        form = SetorForm(request.POST)

        if form.is_valid():
            setor = Setor()
            setor.nome_setor = request.POST['nome_setor']
            setor.localidade = request.POST['localidade']
            setor.telefone = request.POST['telefone']
            setor.save()
            registered = True
            


        else:
            messages.error(request, 'Ocorreu um erro ao cadastrar o Setor. Tente novamente!')
            return redirect('/kilua/controle/add_setor/')



    else:

        form = SetorForm()

    return render(request, 'add_setor.html', {'form':form, 'registered': registered})
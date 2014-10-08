from Kilua.forms import *
from django.contrib import messages
from django.shortcuts import render, redirect

def add_cargo(request):


    if request.method == 'POST':
        form = CargoForm(request.POST)

        if form.is_valid():
            cargo = Cargo()
            cargo.nome_cargo = request.POST['nome_cargo']
            cargo.nivel_cargo = request.POST['nivel_cargo']
            cargo.save()

            messages.success(request, 'Cargo salvo com sucesso!')
            return redirect('/kilua/controle_admin/')

        else:
            messages.error(request, 'Ocorreu um erro ao cadastrar o Cargo. Tente novamente!')
            return redirect('/controle_admin/add_cargo/')



    else:

        form = CargoForm()

    return render(request, 'add_cargo.html', {'form':form})





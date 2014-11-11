from Kilua.forms import *
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def add_cargo(request):

    registered = False

    if request.method == 'POST':
        form = CargoForm(request.POST)

        if form.is_valid():
            cargo = Cargo()
            cargo.nome_cargo = request.POST['nome_cargo']
            cargo.nivel_cargo = request.POST['nivel_cargo']
            cargo.save()

            registered = True





        else:
            messages.error(request, 'Ocorreu um erro ao cadastrar o Cargo. Tente novamente!')
            return redirect('/kilua/controle/add_cargo/')



    else:

        form = CargoForm()

    return render(request, 'add_cargo.html', {'form':form, 'registered': registered})





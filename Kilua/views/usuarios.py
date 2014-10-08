from Kilua.forms import *
from django.contrib import messages
from django.shortcuts import render, redirect

def add_user(request):


    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = Usuario()
            user.nome = request.POST['nome']
            user.email = request.POST['email']
            user.senha = request.POST['senha']
            user.save()

            messages.success(request, 'Usuario salvo com sucesso!')
            return redirect('/kilua/controle_admin/')

        else:
            messages.error(request, 'Ocorreu um erro ao cadastrar o Usuario. Tente novamente!')
            return redirect('/kilua/controle_admin/add_usuario/')



    else:

        form = UserForm()

    return render(request, 'add_usuario.html', {'form':form})
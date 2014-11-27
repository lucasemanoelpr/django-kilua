from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Kilua.models import *
from django.contrib.auth.models import User
#from django.db.models import Q



@login_required
def controle_admin(request):
    context = {}
    chama = []
    lvl = 0
    cham = Chamados.objects.filter(data_termino=None)
    #cham = Chamados.objects.filter(~Q(data_termino=None))

    if len(cham)>0:
        for z in cham:
            chama.append(z.id_prioridade)
    #    chamado_list = Prioridade.objects.all()
    #    for x in chamado_list:
        for x in chama:
            if x.id_user == 1:
                lvl = 20
            else:
                lvl = (Cargo.objects.get(id=(((UserProfile.objects.get(user_id=x.id_user)).codigo_cargo).id)).nivel_cargo)
            x.nivel = ((((Tipo_problema.objects.get(nome_tprob=x.id_tpproblema)).nivel_tprob)*1.5)+(lvl*2))
            x.id_user = (User.objects.get(id=x.id_user))
        #    context['chamados'] = chamado_list
        context['chamados'] = chama

    # id de usuarios tipo 3

    c = UserProfile.objects.filter(codigo_tpuser=3)
    var = []
    for i in c:
         var.append((User.objects.get(username=i.user)).username)

    context['usuarios'] = var

    return render(request, 'controle.html', context)

#def controle_admin(request):
#    context = {}
#    lion = []
#    chamado_list = Prioridade.objects.all()
#    for x in Prioridade.objects.all():
#        lion.append(User.objects.get(id=x.id_user))
#    context['chamados'] = chamado_list
#    context['lion'] = lion
#
#    return render(request, 'controle.html', context)
#
#   return render(request, "controle.html")


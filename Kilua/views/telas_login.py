from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Kilua.models import Prioridade,Chamados,Tipo_problema
from django.contrib.auth.models import User
#from django.db.models import Q


@login_required
def controle_admin(request):
    context = {}
    chama = []
    cham = Chamados.objects.filter(data_termino=None)
    #cham = Chamados.objects.filter(~Q(data_termino=None))

    if len(cham)>0:
        for z in cham:
            chama.append(z.id_prioridade)
    #    chamado_list = Prioridade.objects.all()
    #    for x in chamado_list:
        for x in chama:
            x.id_user = (User.objects.get(id=x.id_user))
            x.nivel = (Tipo_problema.objects.get(nome_tprob=x.id_tpproblema)).nivel_tprob
        #    context['chamados'] = chamado_list
        context['chamados'] = chama

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


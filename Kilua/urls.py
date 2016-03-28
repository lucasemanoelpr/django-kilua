from django.conf.urls import patterns, url
import Kilua.views.login
import Kilua.views.cargo
import Kilua.views.setor
import Kilua.views.usuarios
import Kilua.views.telas_login
import Kilua.views.chamados


urlpatterns = patterns('',


        url(r'^kilua/login/$', Kilua.views.login.logar, name='login'),
        url(r'^kilua/logout/$', Kilua.views.login.user_logout, name='logout'),
        url(r'^kilua/controle/$', Kilua.views.telas_login.controle_admin, name='controle'),
        url(r'^kilua/controle/add_setor/$', Kilua.views.setor.add_setor, name='add_setor'),
        url(r'^kilua/controle/chamado/(?P<chamado_id>\d+)/$', Kilua.views.chamados.visualizar, name='chamado'),
        url(r'^kilua/controle/historico/(?P<historico_id>\d+)/$', Kilua.views.chamados.visualizar_historico, name='historico'),
        url(r'^kilua/controle/add_chamado/$', Kilua.views.chamados.add_chamado, name='add_chamado'),
        url(r'^kilua/controle/add_usuario/$', Kilua.views.usuarios.add_user, name='add_usuario'),
        url(r'^kilua/controle/historico/$', Kilua.views.chamados.historico, name='historico'),
        url(r'^kilua/controle/add_cargo/$', Kilua.views.cargo.add_cargo, name='add_cargo'),


    )
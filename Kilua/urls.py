from django.conf.urls import patterns, url
import Kilua.views.login
import Kilua.views.cargo
import Kilua.views.setor
import Kilua.views.usuarios
import Kilua.views.telas_login

urlpatterns = patterns('',


        url(r'^kilua/login/$', Kilua.views.login.logar, name='login'),
        url(r'^kilua/controle_admin/$', Kilua.views.telas_login.controle_admin, name='controle'),
        url(r'^kilua/controle_admin/add_setor/$', Kilua.views.setor.add_setor, name='add_setor'),
        url(r'^kilua/controle_admin/add_usuario/$', Kilua.views.usuarios.add_user, name='add_usuario'),
        url(r'^kilua/controle_admin/add_cargo/$', Kilua.views.cargo.add_cargo, name='add_cargo'),


    )
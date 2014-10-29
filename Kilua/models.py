from django.db import models
from django.contrib.auth.models import User



class Cargo(models.Model):
    nome_cargo = models.CharField(max_length=30)
    nivel_cargo = models.IntegerField()

    def __unicode__(self):
        return self.nome_cargo

class Setor(models.Model):
    nome_setor = models.CharField(max_length=30)
    localidade = models.CharField(max_length=30)
    telefone = models.IntegerField()

class Tipo_problema(models.Model):
    nome_tprob = models.CharField(max_length=50)
    nivel_tprob = models.IntegerField()

    def __unicode__(self):
        return self.nome_tprob

class Tipo_usuario(models.Model):
    nome_tpuser = models.CharField(max_length=20)

    def __unicode__(self):
        return self.nome_tpuser

class UserProfile(models.Model):

    user = models.OneToOneField(User)
    codigo_tpuser = models.ForeignKey(Tipo_usuario)
    codigo_cargo = models.ForeignKey(Cargo)

    def __unicode__(self):
        return self.user.username


class Prioridade(models.Model):
    id_tpproblema = models.ForeignKey(Tipo_problema)
    comentario = models.CharField(max_length=120)
    desc_problema = models.CharField(max_length=120)

class Chamados(models.Model):
    id_prioridade = models.ForeignKey(Prioridade)
    id_setor = models.ForeignKey(Setor)
    data_inicio = models.DateField()
    data_termino = models.DateField()
    desc_solucao = models.CharField(max_length=120)

class Historico(models.Model):
    id_prioridade = models.ForeignKey(Prioridade)
    id_setor = models.ForeignKey(Setor)
    id_chamado = models.IntegerField()
    data_inicio = models.DateField()
    data_termino = models.DateField()
    desc_solucao = models.CharField(max_length=120)
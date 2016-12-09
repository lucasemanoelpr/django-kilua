# -*- coding: utf-8 -*-
import unittest
from django.test import TestCase
from Kilua.models import Chamados, Prioridade, Setor
from django.test.client import Client
from django.core.urlresolvers import reverse
from Kilua.forms import ChamadosForm
import datetime

class ChamadosTest(unittest.TestCase):
	# Testa um método GET na url de cadastro de Chamado
	def test_get(self):
		c = Client()
		c.login(username='teste', password='teste')

		response = c.get('/kilua/controle/add_chamado/', follow=True)
		self.assertEqual(response.status_code, 200)

	# Testa um método POST na url de cadastro de Chamado
	def test_post(self):
		c = Client()
		c.login(username='teste', password='teste')

		response = c.post('/kilua/controle/add_chamado/', {'id_setor': 'ADM', 'localidade': 'Bloco B', 'telefone': 34440000}, follow=True)
		self.assertEqual(response.status_code, 200) 

	# Models tests
	def test_create_chamado(self, id_prioridade = Prioridade.objects.get(id=1), data_inicio = datetime.datetime.now(), data_termino = datetime.datetime.now(), desc_solucao="Foi atualizado o Java"):
		chamado = Chamados(id_prioridade=id_prioridade, data_inicio=data_inicio, data_termino=data_termino, desc_solucao=desc_solucao)
		return chamado

	def test_chamado_creation(self):
		w = self.test_create_chamado()
		self.assertTrue(isinstance(w, Chamados))
		self.assertEqual(type(w.desc_solucao), str)
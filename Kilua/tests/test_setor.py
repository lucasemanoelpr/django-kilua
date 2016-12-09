# -*- coding: utf-8 -*-
import unittest
from django.test import TestCase
from Kilua.models import Setor 
from django.test.client import Client
from django.core.urlresolvers import reverse
from Kilua.forms import SetorForm

class SetorTest(unittest.TestCase):
	
	# Testa um método GET na url de cadastro de Setor
	def test_get(self):
		c = Client()
		c.login(username='teste', password='teste')

		response = c.get('/kilua/controle/add_setor/', follow=True)
		self.assertEqual(response.status_code, 200)

	# Testa um método POST na url de cadastro de Setor
	def test_post(self):
		c = Client()
		c.login(username='teste', password='teste')

		response = c.post('/kilua/controle/add_setor/', {'nome_setor': 'Administração', 'localidade': 'Bloco B', 'telefone': 34440000}, follow=True)
		self.assertEqual(response.status_code, 200) 

	# Models tests
	def test_create_setor(self, nome_setor="ADM", localidade="Anexo B", telefone=4734446989):
		setor = Setor(nome_setor=nome_setor, localidade=localidade, telefone=telefone)
		return setor

	def test_setor_creation(self):
		w = self.test_create_setor()
		self.assertTrue(isinstance(w, Setor))
		self.assertEqual(w.__unicode__(), w.nome_setor)

	# test form
	def test_valid_form(self):	
	    w = self.test_create_setor()
	    data = {'nome_setor': w.nome_setor, 'localidade': w.localidade, 'telefone': w.telefone}
	    form = SetorForm(data=data)
	    self.assertTrue(form.is_valid())
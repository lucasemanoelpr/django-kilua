# -*- coding: utf-8 -*-
import unittest
from django.test import TestCase
from Kilua.models import Setor, Cargo 
from django.test.client import Client

class LogarTest(unittest.TestCase):
	
	def teste(self):
		c = Client()
		rx = c.login(username='teste', password='teste')
		

class CargoTest(TestCase):
  
  	# Cria um dado no banco de dados temporário, não dará erro se todos os campos estiverem corretos
  	def setUp(self):
		self.p1 = Cargo.objects.create(nome_cargo="Chefe", nivel_cargo=10)
    
	def teste_get(self):
		c = Client()
		c.login(username='teste', password='teste')
		response = self.client.get('/kilua/controle/add_cargo/', follow=True)
		self.assertEqual(response.status_code, 404)

	# Testa um método POST na url de cadastro de setor
	def teste_post(self):
		c = Client()
		c.login(username='teste', password='teste')
		response = c.post('/kilua/controle/add_cargo/', {'nome_cargo': 'Chefe', 'nivel_cargo': 10}, follow=True)
		self.assertEqual(response.status_code, 404) 


class SetorTest(unittest.TestCase):
	
	def setUp(self):
		self.p1 = Setor.objects.create(nome_setor="Administração", localidade="Bloco B", telefone="12345678")

	def teste_get(self):
		c = Client()
		c.login(username='teste', password='teste')

		response = c.get('/kilua/controle/add_setor/', follow=True)
		self.assertEqual(response.status_code, 200)

	def teste_post(self):
		c = Client()
		c.login(username='teste', password='teste')

		response = c.post('/kilua/controle/add_setor/', {'nome_setor': 'Administração', 'localidade': 'Bloco B', 'telefone': 34440000}, follow=True)
		self.assertEqual(response.status_code, 200) 


class ChamadosTest(unittest.TestCase):

	def teste_get(self):
		c = Client()
		c.login(username='teste', password='teste')

		response = c.get('/kilua/controle/add_chamado/', follow=True)
		self.assertEqual(response.status_code, 200)

	def teste_post(self):
		c = Client()
		c.login(username='teste', password='teste')

		response = c.post('/kilua/controle/add_chamado/', {'id_setor': 'ADM', 'localidade': 'Bloco B', 'telefone': 34440000}, follow=True)
		self.assertEqual(response.status_code, 200) 

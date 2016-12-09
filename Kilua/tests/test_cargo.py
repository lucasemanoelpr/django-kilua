# -*- coding: utf-8 -*-
import unittest
from django.test import TestCase
from Kilua.models import Cargo 
from django.test.client import Client
from django.core.urlresolvers import reverse
from Kilua.forms import CargoForm


class CargoTest(TestCase):
  
	# Testa um método GET na url de cadastro de Cargo  
	def test_get(self):
		c = Client()
		c.login(username='teste', password='teste')
		response = self.client.get('/kilua/controle/add_cargo/', follow=True)
		self.assertEqual(response.status_code, 200)

	# Testa um método POST na url de cadastro de Cargo
	def test_post(self):
		c = Client()
		c.login(username='teste', password='teste')
		response = c.post('/kilua/controle/add_cargo/', {'nome_cargo': 'Chefe', 'nivel_cargo': 8}, follow=True)
		self.assertEqual(response.status_code, 200) 

	# test models
	def test_create_cargo(self, nome_cargo="CEO", nivel_cargo=10):
		cargo = Cargo(nome_cargo=nome_cargo, nivel_cargo=nivel_cargo)
		return cargo

	def test_cargo_creation(self):
		w = self.test_create_cargo()
		self.assertTrue(isinstance(w, Cargo))
		self.assertEqual(w.__unicode__(), w.nome_cargo)

	# test forms
	def test_valid_form(self):
	    w = self.test_create_cargo()
	    data = {'nome_cargo': w.nome_cargo, 'nivel_cargo': w.nivel_cargo}
	    form = CargoForm(data=data)
	    self.assertTrue(form.is_valid())
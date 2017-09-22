# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from tipo.models import *

class Pokemons(models.Model):
    nome = models.CharField("Nome", max_length=100)
    slug = models.SlugField("Identificador", max_length=100)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    level_inicial = models.IntegerField('Level Inicial')
    evolucao = models.ForeignKey('self', blank=True, null=True)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado', auto_now=True)

    class Meta:
		verbose_name = 'Pokemon'
		verbose_name_plural = 'Pokemons'
		ordering = ['nome']

    def __str__(self): # __unicode__ no python2
        return self.nome

    def get_absolute_url(self):
        return reverse('pokemon:Pokemons', kwargs={'slug': self.slug})

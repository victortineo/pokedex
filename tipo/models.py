# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

class Tipo(models.Model):
    nome = models.CharField("Nome", max_length=100)
    slug = models.SlugField("Slug", max_length=100, null=True)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado', auto_now=True)

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['nome']

    def __str__(self): # __unicode__ no python2
        return self.nome

    def get_absolute_url(self):
        return reverse('tipo:Tipo', kwargs={'slug': self.slug})

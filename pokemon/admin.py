# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.contrib import admin

class PokemonsAdmin(admin.ModelAdmin):
	list_display = ['nome', 'slug', 'tipo', 'level_inicial', 'evolucao'] # campos que serão exibidos
	search_fields = ['nome', 'slug', 'tipo'] # campos de pesquisa
	list_filter = ['created', 'modified']

admin.site.register(Pokemons, PokemonsAdmin)

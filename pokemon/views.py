# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import *
from tipo.models import *

class ListaPokemons(generic.ListView):

    model = Pokemons
    template_name = 'lista/lista.html'
    context_object_name = 'pokemons'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super(ListaPokemons, self).get_context_data(**kwargs)
        context['tipos'] = Tipo.objects.all()
        return context

class ListaPokemonsCategoria(generic.ListView):

    model = Pokemons
    template_name = 'lista/lista.html'
    context_object_name = 'pokemons'
    paginate_by = 9

    def get_queryset(self):
        return Pokemons.objects.filter(tipo__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(ListaPokemonsCategoria, self).get_context_data(**kwargs)
        context['categoriaAtual'] = get_object_or_404(Tipo, slug = self.kwargs['slug'])
        context['tipos'] = Tipo.objects.all()
        return context

listaPokemonsCategoria = ListaPokemonsCategoria.as_view()
listaPokemons = ListaPokemons.as_view()

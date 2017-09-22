# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

class TipoAdmin(admin.ModelAdmin):
	list_display = ['nome'] # campos que serão exibidos
	search_fields = ['nome'] # campos de pesquisa
	list_filter = ['created', 'modified']

admin.site.register(Tipo, TipoAdmin)

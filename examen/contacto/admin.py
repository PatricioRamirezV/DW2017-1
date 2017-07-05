# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from contacto.models import Contacto

class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido','email', 'telefono', 'direccion')
    #list_filter = ('owner','active')
    search_fields = ('nombre', 'apellido', 'email')

admin.site.register(Contacto, ContactoAdmin)

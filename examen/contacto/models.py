# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from sorl.thumbnail import ImageField

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    telefono = models.IntegerField(default=0)
    direccion = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='images',blank=True,null=True)

    def __str__(self):
        return str(self.id)

# coding=utf-8
from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.db import models

from rest_framework.authtoken.models import Token

# Create your models here.


class UserApp(User):
    nome = models.CharField(verbose_name="Nome", max_length=200, null=False, blank=False)
    email_app = models.CharField(verbose_name="Email", max_length=200, null=True, blank=True)
    senha = models.CharField(verbose_name="Senha", max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.nome

    def __unicode__(self):
        return self.nome




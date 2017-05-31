# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from app import models


@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    pass

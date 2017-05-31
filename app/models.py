# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Item(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    price = models.IntegerField(default=False)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name

class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    deliveryTime = models.DateTimeField()
    address = models.CharField(max_length=100, blank=True, default='')
    quantity = models.IntegerField(default=1)
    item = models.ForeignKey(Item, default="")
    user = models.ForeignKey(User, default="", related_name="orders")

    def __str__(self):
        return "Order: " + str(self.id) + "_Item: " + self.item.name
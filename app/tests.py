# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import test
from django.test import TestCase

from app import models


# Create your tests here.
class ItemsTest(TestCase):
    fixtures = ('items.json', 'orders.json', 'users.json')

    def setUp(self):
        self.client = test.Client()

    def test_RequestAllItems(self):
        self.client.force_login(user=models.User.objects.get(pk=1))
        url = '/items/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 2)

    def test_AddItem(self):
        self.client.force_login(user=models.User.objects.get(pk=1))
        url = '/items/'
        response = self.client.post(url, data={'name':'nameTest','price':'13','description':'testdesc'})
        item = models.Item.objects.get(pk=3)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(item.name,"nameTest")


class OrderTest(TestCase):
    fixtures = ('items.json', 'orders.json', 'users.json')

    def setUp(self):
        self.client = test.Client()

    def test_RequestAllItems(self):
        self.client.force_login(user=models.User.objects.get(pk=3))
        url = '/orders/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 3)

    def test_AddOrder(self):
        self.client.force_login(user=models.User.objects.get(pk=1))
        url = '/orders/'

        response = self.client.post(url, data={"deliveryTime":"2016-03-03T03:03:00Z", "address":"ad", "quantity":"12", "item": "1"})
        order = models.Order.objects.get(pk=7)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(order.user.id, 1)
        self.assertEqual(order.item.id, 1)


class UserOrdersTest(TestCase):
    fixtures = ('items.json', 'orders.json', 'users.json')

    def setUp(self):
        self.client = test.Client()

    def test_RequestUserOrders(self):
        self.client.force_login(user=models.User.objects.get(pk=3))
        url = '/userorders/1/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 1)


class BestUserTest(TestCase):
    fixtures = ('items.json', 'orders.json', 'users.json')

    def setUp(self):
        self.client = test.Client()

    def test_RequestBestUser(self):
        self.client.force_login(user=models.User.objects.get(pk=1))
        url = '/bestuser/2016/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['results'][0]["user_id"], 3)
        self.assertEqual(response.json()['results'][0]["total"], 156)


class AvgSpendingTest(TestCase):
    fixtures = ('items.json', 'orders.json', 'users.json')

    def setUp(self):
        self.client = test.Client()

    def test_RequestAvgSpending(self):
        self.client.force_login(user=models.User.objects.get(pk=1))
        url = '/avgspending/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["results"][1]["user_id"], 1)
        self.assertEqual(response.json()["results"][1]["avg"], 39)


class MonthlyRevReportTest(TestCase):
    fixtures = ('items.json', 'orders.json', 'users.json')

    def setUp(self):
        self.client = test.Client()

    def test_RequestAvgSpending(self):
        self.client.force_login(user=models.User.objects.get(pk=1))
        url = '/avgspending/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["results"][1]["user_id"], 1)
        self.assertEqual(response.json()["results"][1]["avg"], 39)
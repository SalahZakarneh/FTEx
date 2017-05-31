# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import F, Sum, Avg
from django.db.models.functions import TruncMonth
from rest_framework import viewsets, permissions

from app.models import Item, Order
from app.serializers import ItemSerializer, OrderSerializer, BestUserSerializer, AvgSpendinSerializer, \
    MonthlyRevSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class OrderViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        current_user = self.request.user
        if current_user.is_staff:
            return Order.objects.all()
        else:
            return Order.objects.filter(user=current_user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    serializer_class = OrderSerializer

    # public api users can get
    permission_classes = (permissions.IsAuthenticated,)


class UserOrderViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Order.objects.filter(user_id=self.kwargs['userid']).all()

    serializer_class = OrderSerializer

    # public api users can get
    permission_classes = (permissions.AllowAny,)


class RetrieveBestUserViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Order.objects.filter(created__year=self.kwargs["year"]).select_related("user").values('user_id').annotate(total=Sum(F("quantity") * F("item__price"))).order_by("-total")[:1]

    serializer_class = BestUserSerializer
    permission_classes = (permissions.IsAdminUser,)
    http_method_names = ['get']


class AvgSpendingViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Order.objects.select_related("user").values('user_id').annotate(avg=Avg(F("quantity") * F("item__price"))).order_by("-avg")

    serializer_class = AvgSpendinSerializer
    permission_classes = (permissions.IsAdminUser,)
    http_method_names = ['get']


class MonthlyRevReportViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Order.objects.annotate(month=TruncMonth("created")).values("month").annotate(sum=Sum(F("quantity") * F("item__price")))

    serializer_class = MonthlyRevSerializer
    permission_classes = (permissions.IsAdminUser,)
    http_method_names = ['get']

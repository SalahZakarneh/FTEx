from django.contrib.auth.models import User
from rest_framework import serializers

from app.models import Item, Order


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'description', 'price')


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'deliveryTime', 'address', 'quantity', 'item', 'user')


class BestUserSerializer(serializers.ModelSerializer):
    total = serializers.IntegerField()
    bestuser = serializers.SerializerMethodField("get_user")

    def get_user(self, obj):
        return User.objects.filter(id=obj["user_id"]).values("username", "email").first()

    class Meta:
        depth = 1
        model = Order
        fields = ('user_id', "bestuser", 'total')

class AvgSpendinSerializer(serializers.ModelSerializer):
    avg = serializers.FloatField()
    useravg = serializers.SerializerMethodField("get_user")

    def get_user(self, obj):
        return User.objects.filter(id=obj["user_id"]).values("username", "email").first()

    class Meta:
        depth = 1
        model = Order
        fields = ('user_id', 'avg', 'useravg')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email')

class MonthlyRevSerializer(serializers.Serializer):
    sum = serializers.IntegerField()

    class Meta:
        fields = ("sum")

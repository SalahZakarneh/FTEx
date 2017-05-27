from rest_framework import serializers
from app.models import Item


class ItemSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    description = serializers.CharField(style={'base_template': 'textarea.html'})
    price = serializers.IntegerField(required=False)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance

#
# class ItemModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Item
#         fields = ('id', 'name', 'description', 'price')
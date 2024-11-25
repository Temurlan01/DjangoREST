from rest_framework import serializers
from products.models import Pizza


class PizzaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pizza
        fields = (
            'id',
            'name',
            'price',
            'consist',
            'image',
        )

class PizzaDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pizza
        fields = (
            'id',
            'name',
            'price',
            'image',
            'size',
            'weight',
        )
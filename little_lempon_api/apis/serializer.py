from .models import Products
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    """
    ProductsSerializer class
    """
    class Meta:
        """
        Meta class
        """
        model = Products
        fields = ('id', 'name', 'price', 'inventory')
        extra_kwargs = {
            "price": {"min_value": 1},
            "inventory": {"min_value": 0},
            }
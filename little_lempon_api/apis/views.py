from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import Products
from .serializer import ProductSerializer
from rest_framework.response import Response


class ProductViewSet(viewsets.ViewSet):
    """
    ProductViewSet class
    """
    def list(self, request):
        queryset = Products.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def create(self, request):
        data = {
            'name': request.data.get('name'),
            'price': request.data.get('price'),
            'inventory': request.data.get('inventory')
        }
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Products.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=200)

    def update(self, request, pk=None):
        queryset = Products.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

    def destroy(self, request, pk=None):
        queryset = Products.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        product.delete()
        return Response({'message': 'Product deleted successfully!'}, status=204)

# product/viewsets.py

from rest_framework.viewsets import ModelViewSet
from product.models import Product, Category
from product.serializers import ProductSerializer, CategorySerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
from rest_framework import serializers


from .models import Brand, Category, Product, ProductLine

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()
    class Meta: 
        model = Product
        fields = "__all__"


class ProductLineSerializer(serializers.ModelSerializer):
    class Meta:
        product = ProductSerializer()

        model = ProductLine
        fields = "__all__"
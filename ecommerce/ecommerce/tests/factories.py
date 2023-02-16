import factory

from ecommerce.product.models import Category, Product, Brand


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: "Category_%d" % n)



class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand
    name = "test_brand"


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = "test_prod"
    description = "test_description"
    is_digital = True
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)





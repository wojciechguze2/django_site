from django.urls import path

from django_shop.products.views import ProductsViewSet

# products
products = ProductsViewSet.as_view({
    'get': 'list',
})

urlpatterns = [
    path('products', products, name='front_products'),
]

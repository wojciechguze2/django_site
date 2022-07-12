from django.urls import path

from django_shop.products.views import ProductsViewSet, ProductViewSet

# products
products = ProductsViewSet.as_view({
    'get': 'list',
})


product = ProductViewSet.as_view({
    'get': 'retrieve',
})

urlpatterns = [
    path('products', products, name='front_products'),
    path('product/<int:product_id>', product, name='front_product')
]

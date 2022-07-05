from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('django_shop.homepage.urls')),
    re_path('', include('django_shop.products.urls')),  # /products
    re_path('', include('django_shop.gallery.urls')),  # /gallery
]

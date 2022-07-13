from django.urls import include, re_path

urlpatterns = [
    # path('admin/', admin.site.urls),
    re_path('', include('django_shop.homepage.urls')),
    re_path('', include('django_shop.products.urls')),  # /products
    re_path('', include('django_shop.gallery.urls')),  # /gallery
    re_path('', include('django_shop.contact.urls')),  # /contact
    re_path('', include('django_shop.account.urls')),  # /login
    re_path('cms/', include('cms.urls'))
]

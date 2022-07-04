from django.urls import path

from django_shop.homepage.views import HomepageViewSet

# products
homepage = HomepageViewSet.as_view({
    'get': 'retrieve',
})

urlpatterns = [
    path('', homepage, name='front_homepage'),
]

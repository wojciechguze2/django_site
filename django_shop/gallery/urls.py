from django.urls import path

from django_shop.gallery.views import GalleryViewSet

gallery = GalleryViewSet.as_view({
    'get': 'list',
})

urlpatterns = [
    path('gallery', gallery, name='front_gallery'),
]

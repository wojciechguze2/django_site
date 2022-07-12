from django.urls import path

from django_shop.homepage.views import ArticleViewSet, HomepageViewSet

# articles
homepage = HomepageViewSet.as_view({
    'get': 'retrieve',
})

article = ArticleViewSet.as_view({
    'get': 'retrieve',
})

urlpatterns = [
    path('', homepage, name='front_homepage'),
    path('article/<int:article_id>', article, name='front_article'),
]

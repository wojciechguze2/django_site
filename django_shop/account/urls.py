from django.urls import path

from django_shop.account.views import LoginViewSet

# products
login = LoginViewSet.as_view({
    'get': 'login',
    'post': 'login',
})

urlpatterns = [
    path('login', login, name='front_login'),
]

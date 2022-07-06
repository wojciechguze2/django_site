from django.urls import path

from django_shop.account.views import LoginViewSet, RegisterViewSet

login = LoginViewSet.as_view({
    'get': 'login',
    'post': 'login',
})

register = RegisterViewSet.as_view({
    'get': 'register',
    'post': 'register',
})

urlpatterns = [
    path('login', login, name='front_login'),
    path('register', register, name='front_register')
]

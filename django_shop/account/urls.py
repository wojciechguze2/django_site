from django.urls import path

from django_shop.account.views import AccountViewSet, LoginViewSet, RegisterViewSet, logoutView

login = LoginViewSet.as_view({
    'get': 'login',
    'post': 'login',
})

register = RegisterViewSet.as_view({
    'get': 'register',
    'post': 'register',
})

account = AccountViewSet.as_view({
    'get': 'retrieve',
    'post': 'retrieve'  # settings form
})

urlpatterns = [
    path('account', account, name='front_account'),
    path('login', login, name='front_login'),
    path('logout/', logoutView, name='front_logout'),
    path('register', register, name='front_register')
]

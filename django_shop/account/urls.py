from django.urls import path

from django_shop.account.views import AccountViewSet, LoginViewSet, RegisterViewSet, logoutView, \
    PasswordReminderViewSet, PasswordChangeViewSet

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

password_reminder_mail = PasswordReminderViewSet.as_view({
    'get': 'remind_mail',
    'post': 'remind_mail'
})

change_password = PasswordChangeViewSet.as_view({
    'get': 'change_password',
    'post': 'change_password'
})

urlpatterns = [
    path('account', account, name='front_account'),
    path('login', login, name='front_login'),
    path('logout/', logoutView, name='front_logout'),
    path('register', register, name='front_register'),
    path('password-reminder', password_reminder_mail, name='front_password_reminder'),
    path('change-password', change_password, name='front_change_password')
]

from django.urls import path

from django_shop.contact.views import ContactViewSet

contact = ContactViewSet.as_view({
    'get': 'send',
    'post': 'send'
})

urlpatterns = [
    path('contact', contact, name='front_contact'),
]

from django import forms
from django.forms import ModelForm

from django_shop.contact.models import ContactModel


class ContactForm(ModelForm):
    title = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Title'}),
        max_length=255
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'E-mail'}),
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Description'}),
        max_length=2048
    )

    class Meta:
        model = ContactModel
        fields = ['title', 'email', 'description']

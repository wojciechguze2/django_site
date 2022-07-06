from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.username = self.cleaned_data.get('email')

        password_1 = self.cleaned_data.get('password1')
        password_2 = self.cleaned_data.get('password2')

        if password_1 == password_2:
            user.password = make_password(password_1)

        if commit:
            user.save()

        return user

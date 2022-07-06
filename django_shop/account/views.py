# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from rest_framework import viewsets
from rest_framework.request import Request

from django_shop.account.forms import RegisterForm
from django_shop.globals.decorators import exceptions_debugger, login_required
from django_shop.settings import DEFAULT_CURRENCY


class LoginViewSet(viewsets.ViewSet):
    @staticmethod
    @exceptions_debugger()
    def login(request: Request):
        if request.user.is_authenticated:
            return redirect('front_account')

        if request.method == 'POST':
            email = request.POST.get('username')  # email
            password = request.POST.get('password')

            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)

                return redirect('front_homepage')
            else:
                messages.info(request, 'Username or password is incorrect')

        return render(request, 'front_login.html', {})


@exceptions_debugger()
def logoutView(request):
    logout(request)

    return redirect('front_homepage')


class RegisterViewSet(viewsets.ViewSet):
    @staticmethod
    @exceptions_debugger()
    def register(request: Request):
        if request.user.is_authenticated:
            return redirect('front_account')

        form = RegisterForm()

        if request.method == 'POST':
            form = RegisterForm(request.POST)

            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('email')
                messages.success(request, 'Account was created for ' + username)

                return redirect('front_login')

        template_variables = {
            'form': form
        }

        return render(request, 'front_register.html', template_variables)


class AccountViewSet(viewsets.ViewSet):
    @staticmethod
    @exceptions_debugger()
    @login_required()
    def retrieve(request: Request):
        orders = [{
            'id': i,
            'product': {
                'id': i,
                'amount': i + 10,
                'name': 'Product name',
                'thumb_url': 'https://images.unsplash.com/photo-1543373014-cfe4f4bc1cdf?ixlib=rb-1.2.1&ixid'
                             '=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8aGlnaCUyMHJlc29sdXRpb258ZW58MHx8MHx8&w=1000&q=80 '
            },
            'price': 199.99 + i,
            'currency': DEFAULT_CURRENCY,
            'created_at': datetime.now(),
            'status': 10
        } for i in range(10)]

        template_variables = {
            'orders': orders
        }

        return render(request, 'front_account.html', template_variables)
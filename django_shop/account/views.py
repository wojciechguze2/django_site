# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from rest_framework import viewsets
from rest_framework.request import Request

from django_shop.account.forms import RegisterForm
from django_shop.globals.decorators import exceptions_debugger, login_required


class LoginViewSet(viewsets.ViewSet):
    @staticmethod
    @exceptions_debugger()
    def login(request: Request):
        if request.user.is_authenticated:
            return redirect('front_homepage')  # todo: change to orders or account page

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
            return redirect('front_homepage')  # todo: change to orders or account page

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

        template_variables = {

        }

        return render(request, 'front_account.html', template_variables)
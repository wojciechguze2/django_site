# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from rest_framework import viewsets
from rest_framework.request import Request

from django_shop.globals.decorators import exceptions_debugger


class LoginViewSet(viewsets.ViewSet):
    @staticmethod
    @exceptions_debugger()
    def login(request: Request):
        if request.user.is_authenticated:
            return redirect('front_homepage')

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                return redirect('front_account')
            else:
                messages.info(request, 'Username or password is incorrect')

        return render(request, 'front_login.html', {})


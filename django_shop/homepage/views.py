# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.request import Request


class HomepageViewSet(viewsets.ViewSet):

    @staticmethod
    def retrieve(request: Request):
        numbers = [i for i in range(100)]

        return render(request, 'homepage.html', {'gallery': numbers})

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.request import Request

from django_shop.globals.decorators import exceptions_debugger


class DashboardViewSet(viewsets.ViewSet):

    @staticmethod
    @exceptions_debugger()
    def retrieve(request: Request):

        template_variables = {}

        return render(request, 'dashboard.html', template_variables)

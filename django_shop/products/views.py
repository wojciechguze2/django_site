# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.request import Request

from django_shop.globals.decorators import exceptions_debugger
from django_shop.globals.rules import Pagination
from django_shop.products.models import Product
from django_shop.settings import DEFAULT_CURRENCY, DEFAULT_LENGTH_UNIT, DEFAULT_WEIGHT_UNIT


class ProductsViewSet(viewsets.ViewSet):

    @staticmethod
    @exceptions_debugger()
    def list(request: Request):
        products = Product.objects.filter(active=True)
        products = [
            product.to_short_repr()
            for product in products
        ]

        request_page_number = request.GET.get('page')
        pagination = Pagination(products, limit=4, request_page_number=request_page_number)

        template_variables = {
            'products': pagination.page_results,
            'pagination': pagination.get_json(),
            'include_pagination': bool(products)
        }

        if request_page_number:
            return render(request, 'products_content.html', template_variables)

        return render(request, 'products.html', template_variables)


class ProductViewSet(viewsets.ViewSet):

    @staticmethod
    @exceptions_debugger()
    def retrieve(request: Request, product_id: int):
        product = Product.objects.get(id=product_id)
        product_json = product.to_repr()

        template_variables = {
            'product': product_json
        }

        return render(request, 'product.html', template_variables)

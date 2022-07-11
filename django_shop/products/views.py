# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.request import Request

from django_shop.globals.decorators import exceptions_debugger
from django_shop.globals.rules import Pagination
from django_shop.settings import DEFAULT_CURRENCY, DEFAULT_LENGTH_UNIT, DEFAULT_WEIGHT_UNIT


class ProductsViewSet(viewsets.ViewSet):

    @staticmethod
    @exceptions_debugger()
    def list(request: Request):
        products = [
            {
                'id': _,
                'name': 'Product name',
                'short_description': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem '
                                     'Ipsum has been the industrys standard dummy text ever since the 1500s. ',
                'thumb_url': 'https://images.unsplash.com/photo-1543373014-cfe4f4bc1cdf?ixlib=rb-1.2.1&ixid'
                             '=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8aGlnaCUyMHJlc29sdXRpb258ZW58MHx8MHx8&w=1000&q=80 ',
                'price': 12.00,
                'price_promoted': 15.00 if _ % 2 == 0 else 0.00,
                'currency': DEFAULT_CURRENCY,
                'brand_id': _
            }
            for _ in range(10)
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
        template_variables = {
            'product': {
                'id': product_id,
                'name': 'Product name',
                'description': ('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem '
                                'Ipsum has been the industrys standard dummy text ever since the 1500s, '
                                'when an unknown printer took a galley of type and scrambled it to make a type '
                                'specimen book. It has survived not only five centuries, but also the leap into '
                                'electronic typesetting, remaining essentially unchanged. It was popularised in the '
                                '1960s with the release of Letraset sheets containing Lorem Ipsum passages, '
                                'and more recently with desktop publishing software like Aldus PageMaker including '
                                'versions of Lorem Ipsum. ' * 2),
                'short_description': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem '
                                     'Ipsum has been the industrys standard dummy text ever since the 1500s. ',
                'thumb_url': 'https://images.unsplash.com/photo-1543373014-cfe4f4bc1cdf?ixlib=rb-1.2.1&ixid'
                             '=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8aGlnaCUyMHJlc29sdXRpb258ZW58MHx8MHx8&w=1000&q=80 ',
                'price': 12.00,
                'price_promoted': 15.00 if 2 % 2 == 0 else 0.00,
                'price_save': (15.00 if 2 % 2 == 0 else 0.00) - 12.00,
                'currency': DEFAULT_CURRENCY,
                'weight': 2.850,
                'weight_unit': DEFAULT_WEIGHT_UNIT,
                'width': 12.25,
                'height': 10.15,
                'length': 10.00,
                'length_unit': DEFAULT_LENGTH_UNIT,
                'brand': {
                    'id': product_id,
                    'name': 'Brand name',
                    'logo_url': 'https://images.unsplash.com/photo-1543373014-cfe4f4bc1cdf?ixlib=rb-1.2.1&ixid'
                             '=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8aGlnaCUyMHJlc29sdXRpb258ZW58MHx8MHx8&w=1000&q=80 '
                },
                'image_urls': [
                    'https://images.unsplash.com/photo-1543373014-cfe4f4bc1cdf?ixlib=rb-1.2.1&ixid'
                    '=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8aGlnaCUyMHJlc29sdXRpb258ZW58MHx8MHx8&w=1000&q=80 '
                    for _ in range(3)
                ],
                'recommendations': [{
                    'id': i,
                    'thumb_url': 'https://images.unsplash.com/photo-1543373014-cfe4f4bc1cdf?ixlib=rb-1.2.1&ixid'
                    '=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8aGlnaCUyMHJlc29sdXRpb258ZW58MHx8MHx8&w=1000&q=80 '
                } for i in range(12)]
            }
        }

        return render(request, 'product.html', template_variables)

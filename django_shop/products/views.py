# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.request import Request

from django_shop.globals.decorators import exceptions_debugger
from django_shop.globals.rules import Pagination
from django_shop.settings import DEFAULT_CURRENCY


class ProductsViewSet(viewsets.ViewSet):

    @staticmethod
    @exceptions_debugger()
    def list(request: Request):
        products = [
            {
                'id': _,
                'name': 'Product name',
                'description': ('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem '
                                'Ipsum has been the industrys standard dummy text ever since the 1500s, '
                                'when an unknown printer took a galley of type and scrambled it to make a type '
                                'specimen book. It has survived not only five centuries, but also the leap into '
                                'electronic typesetting, remaining essentially unchanged. It was popularised in the '
                                '1960s with the release of Letraset sheets containing Lorem Ipsum passages, '
                                'and more recently with desktop publishing software like Aldus PageMaker including '
                                'versions of Lorem Ipsum. ' * 2),  # not used here
                'short_description': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem '
                                     'Ipsum has been the industrys standard dummy text ever since the 1500s. ',
                'thumb_url': 'https://images.unsplash.com/photo-1543373014-cfe4f4bc1cdf?ixlib=rb-1.2.1&ixid'
                             '=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8aGlnaCUyMHJlc29sdXRpb258ZW58MHx8MHx8&w=1000&q=80 ',
                'price': 12.00,
                'price_promoted': 15.00 if _ % 2 == 0 else 0.00,
                'currency': DEFAULT_CURRENCY,
                'image_urls': [  # not used here
                    'https://images.unsplash.com/photo-1543373014-cfe4f4bc1cdf?ixlib=rb-1.2.1&ixid'
                    '=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8aGlnaCUyMHJlc29sdXRpb258ZW58MHx8MHx8&w=1000&q=80 '
                    for _ in range(3)
                ]
            }
            for _ in range(10)
        ]

        page_number = request.GET.get('page')
        pagination_page_number = int(page_number) if page_number else 1
        pagination = Pagination(products, limit=4, page_number=pagination_page_number)

        template_variables = {
            'products': pagination.page_results,
            'pagination': pagination.get_json(),
            'include_pagination': True
        }

        if page_number:
            return render(request, 'products_content.html', template_variables)

        return render(request, 'products.html', template_variables)

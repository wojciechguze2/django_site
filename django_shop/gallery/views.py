# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.request import Request

from django_shop.globals.decorators import exceptions_debugger
from django_shop.globals.rules import Pagination


class GalleryViewSet(viewsets.ViewSet):

    @staticmethod
    @exceptions_debugger()
    def list(request: Request):
        images = [
            {
                'id': _,
                'title': 'Product name',
                'image_url': 'https://images.unsplash.com/photo-1543373014-cfe4f4bc1cdf?ixlib=rb-1.2.1&ixid'
                             '=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8aGlnaCUyMHJlc29sdXRpb258ZW58MHx8MHx8&w=1000&q=80 ',
            }
            for _ in range(10)
        ]

        page_number = request.GET.get('page')
        pagination_page_number = int(page_number) if page_number else 1
        pagination = Pagination(images, limit=12, page_number=pagination_page_number)

        template_variables = {
            'images': pagination.page_results,
            'pagination': pagination.get_json(),
            'include_pagination': True
        }

        if page_number:
            return render(request, 'gallery_content.html', template_variables)

        return render(request, 'gallery.html', template_variables)

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
            for _ in range(100)
        ]

        request_page_number = request.GET.get('page')
        pagination = Pagination(images, limit=12, request_page_number=request_page_number)

        template_variables = {
            'images': pagination.page_results,
            'pagination': pagination.get_json(),
            'include_pagination': bool(images)
        }

        if request_page_number:
            return render(request, 'gallery_content.html', template_variables)

        return render(request, 'gallery.html', template_variables)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.request import Request

from django_shop.globals.decorators import exceptions_debugger


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

        template_variables = {
            'images': images
        }

        return render(request, 'gallery.html', template_variables)

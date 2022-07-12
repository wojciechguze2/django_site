# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.request import Request

from django_shop.gallery.models import Gallery
from django_shop.globals.decorators import exceptions_debugger
from django_shop.globals.rules import Pagination


class GalleryViewSet(viewsets.ViewSet):

    @staticmethod
    @exceptions_debugger()
    def list(request: Request):
        gallery = Gallery.objects.filter(active=True)
        images = [
            image.to_repr()
            for image in gallery
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

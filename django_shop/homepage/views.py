# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.request import Request


class HomepageViewSet(viewsets.ViewSet):

    @staticmethod
    def retrieve(request: Request):
        articles = [
            {
                'id': _,
                'title': 'Article title',
                'description': ('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem '
                                'Ipsum has been the industrys standard dummy text ever since the 1500s, '
                                'when an unknown printer took a galley of type and scrambled it to make a type '
                                'specimen book. It has survived not only five centuries, but also the leap into '
                                'electronic typesetting, remaining essentially unchanged. It was popularised in the '
                                '1960s with the release of Letraset sheets containing Lorem Ipsum passages, '
                                'and more recently with desktop publishing software like Aldus PageMaker including '
                                'versions of Lorem Ipsum. ' * 15),
                'image_url': 'https://images.unsplash.com/photo-1543373014-cfe4f4bc1cdf?ixlib=rb-1.2.1&ixid'
                             '=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8aGlnaCUyMHJlc29sdXRpb258ZW58MHx8MHx8&w=1000&q=80 '
            }
            for _ in range(9)
        ]

        template_variables = {
            'articles': articles
        }

        return render(request, 'homepage.html', template_variables)

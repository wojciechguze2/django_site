# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.request import Request

from django_shop.globals.rules import Pagination
from django_shop.homepage.models import Article


class HomepageViewSet(viewsets.ViewSet):

    @staticmethod
    def retrieve(request: Request):
        articles = Article.objects.filter(active=True)
        articles = [
            article.to_repr()
            for article in articles
        ]

        request_page_number = request.GET.get('page')
        pagination = Pagination(articles, request_page_number=request_page_number, limit=1)

        template_variables = {
            'articles': pagination.page_results,
            'pagination': pagination.get_json(),
            'include_pagination': bool(articles)
        }

        if request_page_number:
            return render(request, 'articles_content.html', template_variables)

        return render(request, 'homepage.html', template_variables)

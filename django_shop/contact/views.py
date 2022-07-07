# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.request import Request

from django_shop.contact.exceptions import ContactSaveError
from django_shop.contact.forms import ContactForm
from django_shop.globals.decorators import exceptions_debugger


class ContactViewSet(viewsets.ViewSet):

    @staticmethod
    @exceptions_debugger()
    def send(request: Request):
        if request.method == 'POST':
            form = ContactForm(request.POST)

            if form.is_valid():
                try:
                    new_form = form.save(commit=False)
                    new_form.save()
                except Exception as e:
                    raise ContactSaveError

                return HttpResponseRedirect('/contact')

        else:
            form = ContactForm()

        return render(request, 'contact.html', {'form': form})
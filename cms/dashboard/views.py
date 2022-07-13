from datetime import datetime

from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.request import Request

from cms.dashboard import MONTHS
from django_shop.globals.decorators import exceptions_debugger
from django_shop.orders.models import Order


class DashboardViewSet(viewsets.ViewSet):

    @staticmethod
    @exceptions_debugger()
    def retrieve(request: Request):
        today = datetime.today()

        orders = Order.objects.prefetch_related('product')
        orders_data = []
        orders_month_labels = []

        products_orders = orders.values('product_id', 'product__name')
        products_data = {}
        products_labels = []
        products_counts = []

        for month_number in range(1, 12):
            month_orders = orders.filter(
                create_date__year=today.year,
                create_date__month=month_number
            ).count()

            if month_orders:
                orders_data.append(month_orders)
                orders_month_labels.append(MONTHS[month_number - 1])

        for product_orders in products_orders:
            product_id = product_orders.get('product_id')
            product_name = product_orders.get('product__name')

            if product_id not in products_data.keys():
                products_data[product_id] = {
                    'product_name': product_name,
                    'count': 1
                }
            else:
                products_data[product_id]['count'] += 1

        for product_id in products_data.keys():
            products_labels.append(products_data[product_id]['product_name'])
            products_counts.append(products_data[product_id]['count'])

        template_variables = {
            'orders_month_labels': orders_month_labels,
            'orders_data': orders_data,
            'accounts_count': User.objects.all().count(),
            'products_labels': products_labels,
            'products_data': products_counts
        }

        return render(request, 'dashboard.html', template_variables)

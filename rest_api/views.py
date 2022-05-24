from rest_framework import viewsets
from spreadsheet_app.models import Order
from rest_api.serializers import OrderSerializer, OrderChartSerializer
from django.db.models import Count, Sum

from spreadsheet_app.logic.tasks import get_and_write_an_order_in_the_database


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderChartViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.values('delivery_time')\
        .annotate(cost_in_dollar_for_chart=Sum('cost_in_dollar')).order_by('delivery_time')
    serializer_class = OrderChartSerializer

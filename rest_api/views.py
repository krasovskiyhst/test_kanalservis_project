from rest_framework import viewsets
from spreadsheet_app.models import Order
from rest_api.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

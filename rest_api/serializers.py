from rest_framework import serializers
from spreadsheet_app.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderChartSerializer(serializers.ModelSerializer):
    cost_in_dollar_for_chart = serializers.FloatField(required=True)

    class Meta:
        model = Order
        fields = ('delivery_time', 'cost_in_dollar_for_chart')

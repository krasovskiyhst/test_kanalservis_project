from django.contrib import admin
from .models import Order


@admin.register(Order)
class ProductDataOneDay(admin.ModelAdmin):
    list_display = ("id", "order_number", "cost_in_rubles", "cost_in_dollar", "delivery_time")

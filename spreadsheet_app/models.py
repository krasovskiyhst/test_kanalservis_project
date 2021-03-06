from django.db import models


class Order(models.Model):
    order_number = models.PositiveBigIntegerField(verbose_name='Заказ №')
    cost_in_rubles = models.FloatField(verbose_name='Стоимость,руб.')
    cost_in_dollar = models.FloatField(verbose_name='Стоимость,дол.')
    delivery_time = models.DateField(verbose_name='Срок поставки')

    class Meta:
        ordering = ['id']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

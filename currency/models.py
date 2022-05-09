from django.db import models


class Currency(models.Model):
    CURRENCY_TYPE_CHOICES = [
        ('USD', 'Dollar'),
        ('EUR', 'Euro'),
        ('BTC', 'Bitcoin')
    ]

    currency_type = models.CharField(max_length=20, choices=CURRENCY_TYPE_CHOICES)
    buy = models.DecimalField(max_digits=10, decimal_places=4)
    sell = models.DecimalField(max_digits=10, decimal_places=4)
    source = models.CharField(max_length=30)
    exchange_date = models.DateTimeField(auto_now_add=True)

from currency.models import Currency
from decimal import Decimal
from celery import shared_task

import requests


@shared_task
def collect_rates_pb():
    pb_api_url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'

    response = requests.get(pb_api_url)
    rates = response.json()
    for rate in rates:
        currency = rate['ccy']
        buy = Decimal(rate['buy'])
        sell = Decimal(rate['sale'])
        print(currency, buy, sell)
        if currency in ['USD', 'EUR', 'BTC']:
            last_record = Currency.objects.filter(
                currency_type=currency,
                source='PrivatBank').order_by('-exchange_date').first()

            if last_record is None or last_record.buy != buy or last_record.sell != sell:
                object_data = {
                    'currency_type': currency,
                    'buy': buy,
                    'sell': sell,
                    'source': 'PrivatBank'
                }

                Currency.objects.create(**object_data)

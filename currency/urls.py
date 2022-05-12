from django.urls import path

from currency.views import CurrencyListView

app_name = 'currency'

urlpatterns = [
    path('', CurrencyListView.as_view(), name='currency_list')
]
from django.views.generic import ListView

from currency.models import Currency


class CurrencyListView(ListView):
    model = Currency
    template_name = 'currency_list.html'
    queryset = Currency.objects.all().order_by('-exchange_date')
    paginate_by = 10

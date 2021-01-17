from django_filters.rest_framework import CharFilter, FilterSet

from .models import Account


class AccountFilter(FilterSet):
    card = CharFilter(field_name='card', lookup_expr='icontains')

    class Meta:
        fields = ('card',)
        model = Account

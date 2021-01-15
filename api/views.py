from rest_framework import mixins, viewsets

from .filters import AccountFilter
from .models import DIGITS_IN_CARD_NUMBER, Account, Transaction
from .serializers import AccountSerializer, TransactionSerializer


class AccountViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    filterset_class = AccountFilter


class TransactionViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        queryset = Transaction.objects.all()
        card = self.request.query_params.get('card', None)
        if card is not None:
            queryset = queryset.filter(account__card=card.zfill(DIGITS_IN_CARD_NUMBER))
        return queryset

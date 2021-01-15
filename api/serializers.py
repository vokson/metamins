from rest_framework import serializers

from .models import DIGITS_IN_CARD_NUMBER, Account, Transaction


class AccountSerializer(serializers.ModelSerializer):
    def to_internal_value(self, data):
        data['card'] = data['card'].zfill(DIGITS_IN_CARD_NUMBER)
        return super().to_internal_value(data)

    class Meta:
        fields = '__all__'
        model = Account


class TransactionSerializer(serializers.ModelSerializer):
    card = serializers.SlugRelatedField(source='account', slug_field='card', read_only=True)

    class Meta:
        fields = '__all__'
        model = Transaction

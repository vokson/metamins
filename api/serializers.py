from rest_framework import serializers

from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    def to_internal_value(self, data):
        data['card'] = data['card'].zfill(12)
        return super().to_internal_value(data)

    class Meta:
        fields = '__all__'
        model = Account

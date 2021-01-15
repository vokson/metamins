from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from .models import (DIGITS_IN_CARD_NUMBER, Account, Transaction,
                     TransactionType)


class AccountAdminForm(forms.ModelForm):
    card = forms.CharField(
        label='Номер карты',
        validators=[
            RegexValidator(
                regex=r'^[0-9]{1,' + str(DIGITS_IN_CARD_NUMBER) + r'}$',
                message='Номер карты должен состоять из цифр 0-9'
            )
        ]
    )

    class Meta:
        model = Account
        fields = ('card', 'name', 'surname', 'balance', 'phone',)

    def clean_card(self):
        return self.cleaned_data['card'].zfill(DIGITS_IN_CARD_NUMBER)


class TransactiontAdminForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('account', 'type', 'amount',)

    def clean(self):
        cleaned_data = super().clean()
        account = cleaned_data.get('account')
        type = cleaned_data.get('type')
        amount = cleaned_data.get('amount')

        if account and amount and type:
            if type == TransactionType.SUBSTRACT_BONUS and amount.compare(account.balance) == 1:
                raise ValidationError('На балансе недостаточно бонусов', code='invalid')

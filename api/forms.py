from django import forms
from django.core.validators import RegexValidator

from .models import Account


class AccountAdminForm(forms.ModelForm):
    card = forms.CharField(
        validators=[
            RegexValidator(
                regex=r'^[0-9]{1,12}$',
                message='Номер карты должен состоять из цифр 0-9'
            )
        ]
    )

    class Meta:
        model = Account
        fields = ('card', 'name', 'surname', 'balance', 'phone',)

    def clean_card(self):
        return self.cleaned_data['card'].zfill(12)

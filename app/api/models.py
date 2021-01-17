from decimal import Decimal

from django.core.validators import MinValueValidator, RegexValidator
from django.db import models

DIGITS_IN_CARD_NUMBER = 12


class Account(models.Model):
    card = models.CharField(
        verbose_name='Номер карты',
        help_text=f'Введите {DIGITS_IN_CARD_NUMBER}-ти значный номер карты',
        max_length=DIGITS_IN_CARD_NUMBER,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[0-9]{12}$',
                message=f'Номер карты должен состоять из {DIGITS_IN_CARD_NUMBER}-ти цифр 0-9'
            )
        ]
    )

    name = models.CharField(
        verbose_name='Имя',
        help_text='Введите имя',
        max_length=150
    )
    surname = models.CharField(
        verbose_name='Фамилия',
        help_text='Введите фамилию',
        max_length=150,
        db_index=True
    )
    phone = models.CharField(
        verbose_name='Номер телефона',
        help_text='Введите номер телефона, начиная с "+"',
        max_length=12,
        db_index=True,
        validators=[
            RegexValidator(
                regex=r'^\+[1-9]\d{1,14}$',
                message='Введите правильный 15-ти значный телефонный номер'
            )
        ]
    )

    balance = models.DecimalField(
        verbose_name='Бонусный баланс',
        help_text='Введите количество баллов',
        default=0,
        max_length=12,
        max_digits=7,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0'))]
    )

    created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Бонусный Аккаунт'
        verbose_name_plural = 'Бонусные Аккаунты'
        ordering = ['-created']

    def __str__(self) -> str:
        name = self.name
        surname = self.surname
        card = self.card
        return f'{card}: {surname} {name}'


class TransactionType(models.TextChoices):
    MONEY = 'money'
    ADD_BONUS = 'add_bonus'
    SUBSTRACT_BONUS = 'substract_bonus'


TRANSACTION_TYPE_FACTORS = {
    TransactionType.SUBSTRACT_BONUS: -1,
    TransactionType.ADD_BONUS: 1,
    TransactionType.MONEY: 0
}


class Transaction(models.Model):

    account = models.ForeignKey(
        Account,
        verbose_name='Аккаунт',
        help_text='Выберите бонусный аккаунт',
        on_delete=models.CASCADE,
        related_name='transactions'
    )

    type = models.CharField(
        verbose_name='Тип',
        help_text='Выберите тип',
        max_length=30,
        choices=TransactionType.choices,
        default=TransactionType.MONEY
    )

    amount = models.DecimalField(
        verbose_name='Сумма',
        help_text='Введите сумму',
        default=0,
        max_length=12,
        max_digits=7,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0'))]
    )

    date = models.DateTimeField(
        verbose_name='Дата',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'
        ordering = ['-date']

    def __str__(self) -> str:
        account = self.account
        amount = self.amount
        return f'{account}: {amount}'

    def save(self, *args, **kwargs):
        self.account.balance += self.amount * TRANSACTION_TYPE_FACTORS[self.type]
        self.account.save()

        super().save(*args, **kwargs)

from django.db import models
from django.core.validators import RegexValidator


class Account(models.Model):
    card = models.CharField(
        verbose_name='Номер карты',
        help_text='Введите 12-ти значный номер карты',
        max_length=12,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[0-9]{12}$',
                message='Номер карты должен состоять из 12-ти цифр 0-9'
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
        max_length=12,
        max_digits=7,
        decimal_places=2
    )
    created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )

    class Meta:
        ordering = ['-created']

    def __str__(self) -> str:
        name = self.name
        surname = self.surname
        card = self.card
        return f'{card}: {surname} {name}'

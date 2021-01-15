# Generated by Django 3.1.5 on 2021-01-15 12:52

from decimal import Decimal

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.CharField(help_text='Введите 12-ти значный номер карты', max_length=12, unique=True, validators=[django.core.validators.RegexValidator(message='Номер карты должен состоять из 12-ти цифр 0-9', regex='^[0-9]{12}$')], verbose_name='Номер карты')),
                ('name', models.CharField(help_text='Введите имя', max_length=150, verbose_name='Имя')),
                ('surname', models.CharField(db_index=True, help_text='Введите фамилию', max_length=150, verbose_name='Фамилия')),
                ('phone', models.CharField(db_index=True, help_text='Введите номер телефона, начиная с "+"', max_length=12, validators=[django.core.validators.RegexValidator(message='Введите правильный 15-ти значный телефонный номер', regex='^\\+[1-9]\\d{1,14}$')], verbose_name='Номер телефона')),
                ('balance', models.DecimalField(decimal_places=2, default=0, help_text='Введите количество баллов', max_digits=7, max_length=12, validators=[django.core.validators.MinValueValidator(Decimal('0'))], verbose_name='Бонусный баланс')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Бонусный Аккаунт',
                'verbose_name_plural': 'Бонусные Аккаунты',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('money', 'Money'), ('add_bonus', 'Add Bonus'), ('substract_bonus', 'Substract Bonus')], default='money', help_text='Выберите тип', max_length=30, verbose_name='Тип')),
                ('amount', models.DecimalField(decimal_places=2, default=0, help_text='Введите сумму', max_digits=7, max_length=12, validators=[django.core.validators.MinValueValidator(Decimal('0'))], verbose_name='Сумма')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('account', models.ForeignKey(help_text='Выберите бонусный аккаунт', on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='api.account', verbose_name='Аккаунт')),
            ],
            options={
                'verbose_name': 'Транзакция',
                'verbose_name_plural': 'Транзакции',
                'ordering': ['-date'],
            },
        ),
    ]

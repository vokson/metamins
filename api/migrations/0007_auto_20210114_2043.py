# Generated by Django 3.1.5 on 2021-01-14 17:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_account_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.DecimalField(decimal_places=2, help_text='Введите количество баллов', max_digits=7, max_length=12, verbose_name='Бонусный баланс'),
        ),
        migrations.AlterField(
            model_name='account',
            name='card',
            field=models.CharField(help_text='Введите 12-ти значный номер карты', max_length=12, unique=True, validators=[django.core.validators.RegexValidator(message='Номер карты должен состоять из 12-ти цифр 0-9', regex='^[0-9]{12}$')], verbose_name='Номер карты'),
        ),
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(help_text='Введите имя', max_length=150, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=models.CharField(db_index=True, help_text='Введите номер телефона, начиная с "+"', max_length=12, validators=[django.core.validators.RegexValidator(message='Введите правильный 15-ти значный телефонный номер', regex='^\\+[1-9]\\d{1,14}$')], verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='account',
            name='surname',
            field=models.CharField(db_index=True, help_text='Введите фамилию', max_length=150, verbose_name='Фамилия'),
        ),
    ]
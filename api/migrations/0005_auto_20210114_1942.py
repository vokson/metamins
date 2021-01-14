# Generated by Django 3.1.5 on 2021-01-14 16:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210114_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=models.CharField(db_index=True, max_length=12, validators=[django.core.validators.RegexValidator(message='Введите правильный 15-ти значный телефонный номер', regex='^\\+[1-9]\\d{1,14}$')], verbose_name='Номер телефона'),
        ),
    ]
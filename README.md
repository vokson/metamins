# Metamins Test Task 1
Сервис запущен и работает по адресу http://178.154.234.5
Зайти в admin панель можно с помощью данных, отправленных в телеграмме

## Функции REST API
Получить JWT токен с использованием username, password в формате JSON
POST http://178.154.234.5/api/v1/token/
{
    "username": "XXXX",
    "password": "XXXX"
}

Далее все запросы с использование JWT токена. Header: 'Bearer ..'

Получение всех бонусных аккаунтов
GET http://178.154.234.5/api/v1/accounts/

Получение бонусного аккаунта по ID
GET http://178.154.234.5/api/v1/accounts/1/

Получение бонусного аккаунта по номеру карты
GET http://178.154.234.5/api/v1/accounts/?card=1

Создание бонусного аккаунта
POST http://178.154.234.5/api/v1/accounts/
{
    "card": "3",
    "name": "Максим",
    "surname": "Горький",
    "phone": "+79202904022",
    "balance": "9.99"
}

Получение всех транзакций
GET http://178.154.234.5/api/v1/transactions/

Получение всех транзакций по номеру карты
GET http://178.154.234.5/api/v1/transactions/?card=1
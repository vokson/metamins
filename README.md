# Metamins Test Task 1

## DOCKER-COMPOSE DEVELOPMENT MODE
Клонировать репозиторий<br/>
git clone https://github.com/vokson/metamins<br/>
git checkout feature-docker

Исправить строку в файле .env.dev, заменив my.ip.add.ress на IP виртуальной машины<br/>
DJANGO_ALLOWED_HOSTS=my.ip.add.ress localhost 127.0.0.1 [::1]

Добавить права на исполнение<br/>
$ chmod +x app/entrypoint.sh

Запустить контейнеры<br/>
sudo docker-compose exec web python manage.py flush --no-input

Выполнить миграции<br/>
sudo docker-compose exec web python manage.py migrate

Добавить супер пользователя Django<br/>
sudo docker-compose exec web python manage.py createsuperuser

Сервис работает здесь<br/>
Ваш IP:8000/admin

Остановить все контейнеры<br/>
sudo docker-compose down -v

## DOCKER-COMPOSE PRODUCTION MODE

Клонировать репозиторий<br/>
git clone https://github.com/vokson/metamins<br/>
git checkout feature-docker

Исправить строку в файле .env.prod, заменив my.ip.add.ress на IP виртуальной машины<br/>
DJANGO_ALLOWED_HOSTS=my.ip.add.ress localhost 127.0.0.1 [::1]

Добавить права на исполнение<br/>
sudo chmod +x app/entrypoint.prod.sh

Запустить контейнеры<br/>
sudo docker-compose -f docker-compose.prod.yml up -d --build

Выполнить миграции<br/>
sudo docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput

Собрать статику<br/>
sudo docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear

Добавить супер пользователя Django<br/>
sudo docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser

Сервис работает здесь<br/>
Ваш IP/admin

Остановить все контейнеры<br/>
sudo docker-compose -f docker-compose.prod.yml down -v

## Функции REST API
Получить JWT токен с использованием username, password в формате JSON<br/>
POST http://178.154.234.5/api/v1/token/<br/>
```json
{
    "username": "XXXX",
    "password": "XXXX"
}
```

Далее все запросы с использование JWT токена. Header: 'Bearer ..'

Получение всех бонусных аккаунтов<br/>
GET http://178.154.234.5/api/v1/accounts/

Получение бонусного аккаунта по ID<br/>
GET http://178.154.234.5/api/v1/accounts/1/

Получение бонусного аккаунта по номеру карты<br/>
(здесь можно искать по части номера, будут найдены все аккаунты, содержащие данную часть)<br/>
GET http://178.154.234.5/api/v1/accounts/?card=1

Создание бонусного аккаунта<br/>
POST http://178.154.234.5/api/v1/accounts/<br/>
```json
{
    "card": "3",
    "name": "Максим",
    "surname": "Горький",
    "phone": "+79202904022",
    "balance": "9.99"
}
```

Получение всех транзакций<br/>
GET http://178.154.234.5/api/v1/transactions/

Получение всех транзакций по номеру карты<br/>
(здесь введенный номер дополняется нулями слева, чтобы в выдачу попали транзакции только одного аккаунта)<br/>
GET http://178.154.234.5/api/v1/transactions/?card=1
from decimal import Decimal
from rest_framework.reverse import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken

from .models import Account

User = get_user_model()


class ApiTest(APITestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.urls = {
            'token': reverse('token_obtain_pair'),
            'account-create': reverse('accounts-list'),
            'account-list': reverse('accounts-list'),
        }

        cls.username = 'test_user'
        cls.email = 'user@foo.com'
        cls.password = 'test_password'

        cls.user = User.objects.create_user(
            username=cls.username,
            email=cls.email,
            password=cls.password
        )

        cls.token = AccessToken.for_user(cls.user)

    def test_obtain_token_with_autorized_user(self):
        response = self.client.post(self.urls['token'], {
            'username': self.username,
            'password': self.password
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response.data)
        token = response.data['access']
        self.assertTrue(token, self.token)

    def test_obtain_token_with_unautorized_user(self):
        response = self.client.post(self.urls['token'], {
            'username': self.username,
            'password': 'wrong_password'
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_account_with_autorized_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+str(self.token))
        response = self.client.post(self.urls['account-create'], {
            'card': '1',
            'name': 'John',
            'surname': 'Doe',
            'phone': '+79202002020',
            'balance': '100.00',
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Account.objects.count(), 1)

        account = Account.objects.first()
        self.assertEqual(account.card, '000000000001')
        self.assertEqual(account.name, 'John')
        self.assertEqual(account.surname, 'Doe')
        self.assertEqual(account.phone, '+79202002020')
        self.assertEqual(account.balance, Decimal('100.00'))

    def test_create_account_with_wrong_card(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+str(self.token))
        response = self.client.post(self.urls['account-create'], {
            'card': 'A',
            'name': 'John',
            'surname': 'Doe',
            'phone': '+79202002020',
            'balance': '100.00',
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Account.objects.count(), 0)

    def test_create_account_with_wrong_name(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+str(self.token))
        response = self.client.post(self.urls['account-create'], {
            'card': '1',
            'surname': 'Doe',
            'phone': '+79202002020',
            'balance': '100.00',
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Account.objects.count(), 0)

    def test_create_account_with_wrong_surname(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+str(self.token))
        response = self.client.post(self.urls['account-create'], {
            'card': '1',
            'name': 'John',
            'phone': '+79202002020',
            'balance': '100.00',
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Account.objects.count(), 0)

    def test_create_account_with_wrong_phone(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+str(self.token))
        response = self.client.post(self.urls['account-create'], {
            'card': '1',
            'name': 'John',
            'surname': 'Doe',
            'phone': '79202002020',
            'balance': '100.00',
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Account.objects.count(), 0)

    def test_create_account_with_wrong_balance(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+str(self.token))
        response = self.client.post(self.urls['account-create'], {
            'card': '1',
            'name': 'John',
            'surname': 'Doe',
            'phone': '+79202002020',
            'balance': '-0.01',
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Account.objects.count(), 0)

    def test_create_account_with_unautorized_user(self):
        response = self.client.post(self.urls['account-create'], {
            'card': '1',
            'name': 'John',
            'surname': 'Doe',
            'phone': '+79202002020',
            'balance': '100.00',
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Account.objects.count(), 0)

    def test_list_account_with_autorized_user(self):
        Account.objects.create(
            card='000000000001',
            name='John',
            surname='Doe',
            phone='+79202002020',
            balance=Decimal('100.00')
        )

        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+str(self.token))
        response = self.client.get(self.urls['account-list'], format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        account = response.data[0]
        self.assertEqual(account.get('card'), '000000000001')
        self.assertEqual(account.get('name'), 'John')
        self.assertEqual(account.get('surname'), 'Doe')
        self.assertEqual(account.get('phone'), '+79202002020')
        self.assertEqual(account.get('balance'), '100.00')

    def test_list_account_with_unautorized_user(self):
        response = self.client.get(self.urls['account-list'], format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_account_by_card_with_autorized_user(self):
        Account.objects.create(
            card='000000000123',
            name='John',
            surname='Doe',
            phone='+79202002020',
            balance=Decimal('100.00')
        )

        Account.objects.create(
            card='000000000456',
            name='Mike',
            surname='Smith',
            phone='+12369',
            balance=Decimal('333.33')
        )

        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+str(self.token))
        response = self.client.get(
            self.urls['account-list'],
            data={'card': '123'},
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        account = response.data[0]
        self.assertEqual(account.get('card'), '000000000123')
        self.assertEqual(account.get('name'), 'John')
        self.assertEqual(account.get('surname'), 'Doe')
        self.assertEqual(account.get('phone'), '+79202002020')
        self.assertEqual(account.get('balance'), '100.00')

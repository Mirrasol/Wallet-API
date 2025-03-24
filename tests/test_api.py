from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from api.models import Wallets
from decimal import Decimal


class WalletsTestCase(APITestCase):
    fixtures = ['wallets.json']

    def setUp(self):
        self.client = APIClient()
        self.wallet1 = Wallets.objects.get(uuid='74417945-fe0d-45e3-9cdb-025dc65711aa')
        self.wallet2 = Wallets.objects.get(uuid='ff8ea749-761a-4dcf-b880-1b7338f2711c')
        self.wallet3 = Wallets.objects.get(uuid='661d3d13-9a52-4151-9d4f-8f4e9d1dc491')

    def test_get_wallet_balance(self):
        """
        Ensure we can get the current balance of a wallet.
        """
        url = f'/api/v1/wallets/{self.wallet1.uuid}/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['balance'], '0.000')

    def test_deposit_funds(self):
        """
        Ensure we can deposit a valid sum into a wallet.
        """
        url = f'/api/v1/wallets/{self.wallet2.uuid}/operation/'
        data = {"operation_type": "DEPOSIT", "amount": 5}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['detail'], 'Operation successful.')
        self.assertEqual(
            Wallets.objects.get(uuid='ff8ea749-761a-4dcf-b880-1b7338f2711c').balance,
            Decimal('15.765'),
        )

    def test_withdraw_funds(self):
        """
        Ensure we can withdraw a valid sum from a wallet.
        """
        url = f'/api/v1/wallets/{self.wallet3.uuid}/operation/'
        data = {"operation_type": "WITHDRAW", "amount": 100}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['detail'], 'Operation successful.')
        self.assertEqual(
            Wallets.objects.get(uuid='661d3d13-9a52-4151-9d4f-8f4e9d1dc491').balance,
            Decimal('16.364'),
        )

    def test_use_isufficient_funds_amount(self):
        """
        Check that we can cannot withdraw an insufficient sum.'
        """
        url = f'/api/v1/wallets/{self.wallet1.uuid}/operation/'
        data = {"operation_type": "WITHDRAW", "amount": 1000}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], 'Insufficient funds.')

    def test_user_invalid_funds_amount(self):
        """
        Check that we can cannot withdraw or deposit an invalid sum.'
        """
        url = f'/api/v1/wallets/{self.wallet1.uuid}/operation/'
        data = {"operation_type": "WITHDRAW", "amount": -5}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], 'Invalid operation or amount.')

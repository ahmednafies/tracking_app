import datetime
from django.contrib.auth import get_user_model
from shipments.models import Company, Shipment
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status
from rest_framework_jwt.settings import api_settings

User = get_user_model()
payload_handler = api_settings.JWT_PAYLOAD_HANDLER
encode_handler = api_settings.JWT_ENCODE_HANDLER


class ShipmentAPITestCase(APITestCase):
    def setUp(self):
        user = User(username='testuser', email='test@test.com')
        user.set_password("randompassword")
        user.save()

        swedbank = Company.objects.create(
            name="Swedbank",
            address="some address"
        )

        kuhne = Company.objects.create(
            name="Kuhne",
            address="some another address"
        )

        shipment = Shipment.objects.create(
            tracking_no='ULN8947598sdf',
            sender=kuhne,
            receiver=swedbank,
            shipping_date=datetime.datetime(day=1, month=2, year=2018),
            delivery_date=datetime.datetime(day=3, month=2, year=2018),
            status="Shipped",
            product="watch"
        )

    def test_company(self):
        company = Company.objects.first()
        self.assertEqual(company.name, 'Swedbank')

    def test_get_companies(self):
        """
        test companies listing
        no authorization required
        """
        data = {}
        url = api_reverse("api-v2:Create-List-Companies")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_companies(self):
        """
        Test Unauthorized company creation
        """
        data = {
            "name": "Swedbank",
            "address": "some address"
        }
        url = api_reverse("api-v2:Create-List-Companies")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_companies(self):
        """
        Test unauthorized update
        """
        company = Company.objects.first()
        url = company.get_api_url()
        data = {
            "name": "Swedbank",
            "address": "some address"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_companies_with_authentication(self):
        """
        Test Authentication and update a company
        """
        company = Company.objects.first()
        url = company.get_api_url()
        user_obj = User.objects.first()
        payload = payload_handler(user_obj)
        token = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)

        data = {
            "name": "anotherbank",
            "address": "another address"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], data["name"])
        self.assertEqual(response.data["address"], data["address"])

    def test_create_companies_with_authentication(self):
        """
        test authentication and create a company
        """
        url = api_reverse("api-v2:Create-List-Companies")
        user_obj = User.objects.first()
        payload = payload_handler(user_obj)
        token = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        data = {
            "name": "Telia",
            "address": "Telia's address"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], data["name"])
        self.assertEqual(response.data["address"], data["address"])


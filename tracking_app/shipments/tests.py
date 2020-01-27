from django.contrib.auth.models import User
from django.test import Client, TestCase

from shipments.models import Shipment


class DashboardTestCase(TestCase):

    fixtures = ['shipments/fixtures/initial.json']

    def setUp(self):
        super().setUp()

        username, password = 'kuhne', 'kuhne123'
        User.objects.create_user(username=username, email='info@kuhnenagel.ee', password=password)

        self.authenticated_client = Client()
        self.authenticated_client.login(username=username, password=password)

    def test_dashboard_requires_authentication(self):

        # Anonymous users can't see the dashboard

        client = Client()
        response = client.get('/dashboard/')
        self.assertRedirects(response, '/login/?next=/dashboard/')

        # Authenticated users can see the dashboard

        response = self.authenticated_client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)

    def test_shipments_on_dashboard(self):

        # There are 3 shipments on the dashboard (loaded from the fixtures)

        response = self.authenticated_client.get('/dashboard/')
        shipments = response.context['shipments']
        self.assertEqual(len(shipments), 6)



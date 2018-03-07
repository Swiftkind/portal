from django.test import Client, TestCase
from django.urls import reverse
from django.utils import timezone

from users.models import User
from invoices.models import Invoice


date = timezone.now().date()
invoice_data = {
    'order_id':"12",
    'invoice_date':date,
    'terms':"Due of Receipt",
    'due_date':date + timezone.timedelta(days=5),
    'notes':"sample notes",
    'conditions':"condition 1",
    'date_created':date,
    'date_updated':date,
    'status':"Sent"
}


user_data = {
    'email': "john@doe.com",
    'first_name': "John",
    'last_name': "Doe",
    'password': 'password'
}


class DashboardTestCase(TestCase):
    """ Test dashboard
    """
    def setUp(self):
        user = User.objects.create_user(**user_data)
        self.client = Client()
        self.client.login(email=user_data['email'], password=user_data['password'])

    def test_dashboard_not_authenticated(self):
        """ Test dashboard with user not authenticated
        """
        self.client.logout()
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)

    def test_dashboard_authenticated(self):
        """ Test dashboard with user authenticated
        """
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_invoice_empty(self):
        """ Test 
        """
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.context['invoices'].count(), 0)

    def test_invoice_count(self):
        """ Test the invoice number of users
        """
        Invoice.invoice_objects.create(code='abcd', **invoice_data)
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.context['invoices'].count(), 1)


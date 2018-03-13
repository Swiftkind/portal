import json
from django.urls import reverse
from django.utils import timezone
from django.test import TestCase, Client
from invoices.models import Invoice, Item
from users.models import User


date_now = timezone.now().date()

invoice_data = {
    'order_id':"12",
    'invoice_date':date_now,
    'terms':Invoice.DUE_RECEIPT,
    'due_date':date_now + timezone.timedelta(days=5),
    'notes':"sample notes",
    'conditions':"condition 1",
    'date_created':date_now,
    'date_updated':date_now,
    'status':Invoice.SENT
}

user_data = {
    'email': 'john@john.com',
    'first_name': "John",
    'last_name': "Doe",
    'password': User.objects.make_random_password()
}


class InvoiceListTestCase(TestCase):
    """ Test case for invoice list page and invoice detail
    """

    def setUp(self):
        self.client = Client()
        user = User.objects.create_user(**user_data)
        self.client.login(email=user_data['email'], password=user_data['password'])
        self.code = User.objects.make_random_password()
        Invoice.objects.create(code=self.code, **invoice_data)

    def test_invoice_page_authenticated_success(self):
        """ Test for invoice list page with authenticated user
        """
        response = self.client.get(reverse('invoice'))
        self.assertEqual(response.status_code, 200)

    def test_invoice_page_not_authenticated_fail(self):
        """ Test for the invoice list page with unathenticated user
        """
        self.client.logout()
        response = self.client.get(reverse('invoice'))
        self.assertEqual(response.status_code, 302)

    def test_invoice_page_with_1_invoice_success(self):
        """ Test for the invoice list with 1 existing invoice
        """
        response = self.client.get(reverse('invoice'))
        self.assertEqual(response.context['invoices'].count(), 1)

    def test_invoice_get_detail_success(self):
        """ Test for the getting the detail of invoice
        """
        response = self.client.get(reverse('invoice-detail', kwargs={'id':2}))
        self.assertEqual(json.loads(response.content)['code'], self.code)

    def test_invoice_get_detail_not_existing_fail(self):
        """ Test for getting detail of invoice but not existing
        """
        response = self.client.get(reverse('invoice-detail', kwargs={'id':34}))
        self.assertEqual(response.status_code, 404)

import datetime

from django.test import TestCase
from django.urls import reverse


from invoices.models import Invoice
from users.models import User


date = datetime.datetime.now()
invoice_data = {
    'order_id':"12",
    'invoice_date':date,
    'terms':"Due of Receipt",
    'due_date':date + datetime.timedelta(days=5),
    'notes':"sample notes",
    'conditions':"condition 1",
    'date_created':date,
    'date_updated':date,
    'status':"Sent"
}


class DashboardTestCase(TestCase):
    """ Test dashboard
    """
    def setUp(self):
        """ Setup dashboard url
        """
        self.url = reverse('dashboard')

    def test_dashboard(self):
        """ Test dashboard accessibility
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_no_invoice(self):
        """ Test dashboard with empty invoice
        """
        response = self.client.get(self.url)
        self.assertContains(response, Invoice.NO_INVOICE)

    def test_one_invoice(self):
        """ Test dashboard with added invoice
        """
        code = User.objects.make_random_password()
        Invoice.objects.create(code=code, **invoice_data)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, code)

    def test_two_invoice(self):
        """ Test dashboard with multiple added invoice
        """
        code_1 = User.objects.make_random_password()
        Invoice.objects.create(code=code_1, **invoice_data)
        code_2 = User.objects.make_random_password()
        Invoice.objects.create(code=code_2, **invoice_data)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, code_1)
        self.assertContains(response, code_2)

    def test_invoice_url(self):
        """ Test dashboard with invoice url.
            In this example, it will raise 404 since viewing invoice
            is not created yet.
        """
        code = User.objects.make_random_password()
        invoice = Invoice.objects.create(code=code, **invoice_data)

        response = self.client.get(invoice.get_absolute_url())
        self.assertEqual(response.status_code, 404)







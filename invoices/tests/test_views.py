import json
from django.urls import reverse
from django.utils import timezone
from django.test import TestCase, Client
from invoices.models import Invoice, Item
from users.models import User
from customers.models import Customer


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
    'email':'john@john.com',
    'first_name':"John",
    'last_name':"Doe",
    'password':User.objects.make_random_password()
}

customer_data = {
    'email':'dwayne@wade.com',
    'billing_address':'Davao City'
}

api_invoice_data = {
    'order_id':"12",
    'invoice_date':'2018-03-04 06:00:00.000000',
    'terms':Invoice.DUE_RECEIPT,
    'due_date':'2018-03-04 06:00:00.000000',
    'notes':"sample notes",
    'conditions':"condition 1",
    'date_created':'2018-03-04 06:00:00.000000',
    'date_updated':'2018-03-04 06:00:00.000000',
    'status':Invoice.SENT
}


class InvoiceListTestCase(TestCase):
    """ Test case for invoice list page and invoice detail
    """

    def setUp(self):
        self.client = Client()
        self.customer = Customer.objects.create(**customer_data)
        user = User.objects.create_user(**user_data)
        self.client.login(email=user_data['email'], password=user_data['password'])
        self.code = User.objects.make_random_password()
        self.invoice = Invoice.objects.create(code=self.code, **invoice_data, customer=self.customer)

    def test_invoice_page_authenticated_success(self):
        """ Test for invoice list page with authenticated user
        """
        response = self.client.get(reverse('invoices'))
        self.assertEqual(response.status_code, 200)

    def test_invoice_page_not_authenticated_fail(self):
        """ Test for the invoice list page with unathenticated user
        """
        self.client.logout()
        response = self.client.get(reverse('invoices'))
        self.assertEqual(response.status_code, 302)

    def test_invoice_page_with_1_invoice_success(self):
        """ Test for the invoice list with 1 existing invoice
        """
        response = self.client.get(reverse('invoices'))
        self.assertEqual(json.loads(response.content)['result'][0]['order_id'], '12')

    def test_invoice_get_detail_success(self):
        """ Test for the getting the detail of invoice
        """
        response = self.client.get(reverse('invoice', kwargs={'inv_id':self.invoice.id}))
        self.assertEqual(json.loads(response.content)['code'], self.code)

    def test_invoice_get_detail_not_existing_fail(self):
        """ Test for getting detail of invoice but not existing
        """
        response = self.client.get(reverse('invoice', kwargs={'inv_id':34}))
        self.assertEqual(response.status_code, 404)

    def test_invoice_create_success(self):
        """ Test for creating invoice
        """
        api_invoice_data['code'] = self.code
        api_invoice_data['customer'] = self.customer.pk
        response = self.client.post(reverse('invoices'), api_invoice_data)
        self.assertEqual(response.status_code, 201)

    def test_invoice_create_fail(self):
        """ Test for creating invoice with no customer 
        """
        api_invoice_data['code'] = self.code
        response = self.client.post(reverse('invoices'), api_invoice_data)
        self.assertEqual(json.loads(response.content)['customer'][0], "This field is required.")
        self.assertEqual(response.status_code, 400)

    def test_invoice_update_success(self):
        """ Test for updating invoice
        """
        api_invoice_data['code'] = self.code
        api_invoice_data['customer'] = self.customer.pk
        response = self.client.post(reverse('invoices'), api_invoice_data)
        invoice = json.loads(response.content)
        self.assertEqual(response.status_code, 201)

        new_condition = 'condition 2'
        invoice['conditions'] = new_condition
        url = reverse('invoice', kwargs={'inv_id':self.invoice.id})
        response = self.client.patch(url, data=json.dumps(invoice), content_type='application/json')
        self.assertEqual(json.loads(response.content)['conditions'], new_condition)

    def test_invoice_update_fail(self):
        """ Test for updating invoice no code
        """
        api_invoice_data['code'] = self.code
        api_invoice_data['customer'] = self.customer.pk
        response = self.client.post(reverse('invoices'), api_invoice_data)
        invoice = json.loads(response.content)
        self.assertEqual(response.status_code, 201)

        invoice['customer'] = None
        url = reverse('invoice', kwargs={'inv_id':self.invoice.id})
        response = self.client.patch(url, data=json.dumps(invoice), content_type='application/json')
        self.assertEqual(json.loads(response.content)['customer'][0], 'This field may not be null.')
        self.assertEqual(response.status_code, 400)

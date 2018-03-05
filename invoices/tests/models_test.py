import datetime
from django.test import TestCase
from django.db import IntegrityError
from django.contrib.auth.models import User
from invoices.models import Invoice


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


class InvoiceTestCase(TestCase):
    """ Test the model Invoice
    """
    def test_string_repr(self):
        """ check the string representation of the model
        """
        invoice = Invoice(**invoice_data)
        self.assertEqual(str(invoice), invoice.code)

    def test_create_invoice(self):
        """ Create invoice and save to database
        """
        code = User.objects.make_random_password()
        invoice = Invoice.objects.create(code=code, **invoice_data)

        self.assertTrue(isinstance(invoice, Invoice))
        self.assertEqual(invoice.__str__(), code)

    def test_update_invoice(self):
        """ Updates the existing invoice and save to database
        """
        code = User.objects.make_random_password()
        invoice = Invoice.objects.create(code=code, **invoice_data)

        self.assertTrue(isinstance(invoice, Invoice))

        order_id = '43'
        invoice.order_id = order_id
        invoice.save()

        self.assertTrue(invoice.__str__(), code)
        self.assertEqual(invoice.order_id, order_id)

    def test_delete_invoice(self):
        """ Deletes an existing invoice in database
        """
        code = User.objects.make_random_password()
        invoice = Invoice.objects.create(code=code, **invoice_data)

        self.assertTrue(isinstance(invoice, Invoice))

        # Deletes the data
        invoice.delete()

        with self.assertRaises(Invoice.DoesNotExist):
            Invoice.objects.get(code=code)

    def test_creates_invoice_fails(self):
        """ Creates an invoice with no code
        """
        with self.assertRaises(IntegrityError):
            invoice = Invoice.objects.create(code=None,**invoice_data)

    def test_update_invoice_fails(self):
        """ Updates the existing invoice with blank terms
            and save to database
        """
        code = User.objects.make_random_password()
        invoice = Invoice.objects.create(code=code, **invoice_data)

        self.assertTrue(isinstance(invoice, Invoice))

        with self.assertRaises(IntegrityError):
            invoice.terms = None
            invoice.save()

    def test_delete_invoice_fail(self):
        """ Deletes an item that doesn't exist
        """
        code = User.objects.make_random_password()
        invoice = Invoice.objects.create(code=code, **invoice_data)

        self.assertTrue(isinstance(invoice, Invoice))

        with self.assertRaises(Invoice.DoesNotExist):
            fake_invoice = Invoice.objects.get(code="fake_code")
            fake_invoice.delete()
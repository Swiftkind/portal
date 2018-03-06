import datetime
from django.test import TestCase
from django.db import IntegrityError
from users.models import User
from invoices.models import Invoice, Item


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

item_data = {
    'details':"sample detail",
    'quantity':2,
    'rate':45
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

        order_id = 'abc43'
        invoice.order_id = order_id
        invoice.save()

        self.assertEqual(invoice.__str__(), code)
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

    def test_create_invoice_fails(self):
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
            new_invoice = Invoice.objects.get(code="aasd345")
            new_invoice.delete()


class ItemTestCase(TestCase):
    """ For Item model test cases
    """
    def setUp(self):
        code = User.objects.make_random_password()
        self.invoice = Invoice.objects.create(code=code, **invoice_data)

    def test_string_repr(self):
        """ check the string representation of the model
        """
        item = Item(invoice=self.invoice, **item_data)
        self.assertEqual(str(item), str(item.invoice))

    def test_create_item(self):
        """Create item
        """
        item = Item.objects.create(invoice=self.invoice, **item_data)

        self.assertTrue(isinstance(item, Item))
        self.assertEqual(item.__str__(), str(item.invoice))

    def test_update_item(self):
        """ Updates an existing item
        """
        item = Item.objects.create(invoice=self.invoice, **item_data)

        self.assertTrue(isinstance(item, Item))

        new_detail = "Front end design"
        item.details = new_detail
        item.save()

        self.assertEqual(item.__str__(), str(item.invoice))
        self.assertEqual(item.details, new_detail)

    def test_delete_item(self):
        """ Delete an existing item
        """
        item = Item.objects.create(invoice=self.invoice, **item_data)

        self.assertTrue(isinstance(item, Item))

        item.delete()

        with self.assertRaises(Item.DoesNotExist):
            Item.objects.get(invoice=self.invoice)

    def test_create_item_fail(self):
        """ Create an item without invoice
        """
        with self.assertRaises(IntegrityError):
            Item.objects.create(invoice=None, **item_data)

    def test_update_item_fail(self):
        """ Updates an item with details and quantity
        """
        item = Item.objects.create(invoice=self.invoice, **item_data)

        self.assertTrue(isinstance(item, Item))

        with self.assertRaises(IntegrityError):
            item.quantity = -1
            item.save()

    def test_delete_item_fail(self):
        """ Delete an item that doesn't exist
        """
        item = Item.objects.create(invoice=self.invoice, **item_data)

        self.assertTrue(isinstance(item, Item))

        with self.assertRaises(Item.DoesNotExist):
            new_invoice = Invoice(code="asdfdf123", **invoice_data) 
            item = Item.objects.get(invoice=new_invoice)
            item.delete()

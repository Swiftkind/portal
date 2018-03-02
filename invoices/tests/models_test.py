from django.test import TestCase
from invoices.models import Invoice, Item
import datetime

class InvoiceTestCase(TestCase):
    """ Test case for invoice model
    """

    def setUp(self):
        date = datetime.datetime.now()
        Invoice.objects.create(
            code = "1234sdfg",
            order_id = "12",
            invoice_date = date,
            terms ='Due of Receipt',
            due_date = date + datetime.timedelta(days=5),
            notes = "sample notes",
            conditions = "condition 1",
            date_created = date,
            date_updated = date,
            status = "Sent"
        )

        self.data = Invoice.objects.last()

    def test_add_invoice(self):
        self.assertEqual(self.data.code, '1234sdfg')

    def test_edit_invoice(self):
        invoice = self.data
        invoice.code = "new_code"
        invoice.order_id = "11"
        invoice.save()
        new_invoice = Invoice.objects.last()
        self.assertEqual(new_invoice.code, "new_code")

    def test_delete_invoice(self):
        invoice = Invoice.objects.get(code="1234sdfg")
        invoice.delete()

        data = Invoice.objects.all()
        self.assertEqual(data.count(), 0)


class InvoiceItemTestCase(TestCase):
    """ Test case for Item in voice
    """

    def setUp(self):
        date = datetime.datetime.now()
        invoice = Invoice.objects.create(
            code = "1234sdfg",
            order_id = "12",
            invoice_date = date,
            terms ='Due of Receipt',
            due_date = date + datetime.timedelta(days=5),
            notes = "sample notes",
            conditions = "condition 1",
            date_created = date,
            date_updated = date,
            status = "Sent"
        )
        Item.objects.create(
                invoice = invoice,
                details = "Detail sample",
                quantity = 12,
                rate = 45
            )

        self.data = Item.objects.last()

    def test_add_item(self):
        self.assertEqual(self.data.invoice.code, "1234sdfg")

    def test_edit_item(self):
        item = self.data
        item.details = "New detail"
        item.save()

        new_item = Item.objects.last()
        self.assertEqual(new_item.details, "New detail")

    def test_delete_item(self):
        item = self.data
        item.delete()

        data = Item.objects.all()
        self.assertEqual(data.count(), 0)
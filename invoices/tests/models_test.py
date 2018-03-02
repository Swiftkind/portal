from django.test import TestCase
from invoices.models import Invoice
import datetime

class InvoiceTestCase(TestCase):

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

    def test_add_invoice(self):
        data = Invoice.objects.last()
        self.assertEqual(data.code, '1234sdfg')

    def test_edit_invoice(self):
        invoice = Invoice.objects.get(code="1234sdfg")
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
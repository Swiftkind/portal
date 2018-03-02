from django.test import TestCase
from invoices.models import Invoice, Item
import datetime


class InvoiceData(object):
    """ Invoice data and create invoice
    """
    date = datetime.datetime.now()
    invoice_data = {
        'code':"1234ssdsd",
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

    def create_invoice(self):
        data = Invoice.objects.create(
                code = self.invoice_data['code'],
                order_id = self.invoice_data['order_id'],
                invoice_date = self.invoice_data['invoice_date'],
                terms = self.invoice_data['terms'],
                due_date = self.invoice_data['due_date'],
                notes = self.invoice_data['notes'],
                conditions = self.invoice_data['conditions'],
                date_created = self.invoice_data['date_created'],
                date_updated = self.invoice_data['date_updated'],
                status = self.invoice_data['status']
            )
        return data


class InvoiceDataFails(object):
    """ Invoice data with errors and create invoice
    """
    date = datetime.datetime.now()
    invoice_data = {
        'code':None,
        'order_id':"12",
        'invoice_date':None,
        'terms':"Due of Receipt",
        'due_date':None,
        'notes':"sample notes",
        'conditions':"condition 1",
        'date_created':date,
        'date_updated':date,
        'status':"Sent"
    }

    def create_invoice(self):
        data = Invoice.objects.create(
                code = self.invoice_data['code'],
                order_id = self.invoice_data['order_id'],
                invoice_date = self.invoice_data['invoice_date'],
                terms = self.invoice_data['terms'],
                due_date = self.invoice_data['due_date'],
                notes = self.invoice_data['notes'],
                conditions = self.invoice_data['conditions'],
                date_created = self.invoice_data['date_created'],
                date_updated = self.invoice_data['date_updated'],
                status = self.invoice_data['status']
            )
        return data


class InvoiceTestCaseSuccess(TestCase, InvoiceData):
    """ Test case for invoice model
    """
    def setUp(self):
        self.create_invoice()

    def test_add_invoice(self):
        invoice = Invoice.objects.get(code=self.invoice_data['code'])
        self.assertEqual(invoice.code, self.invoice_data['code'])

    def test_edit_invoice(self):
        new_code = "new_code"
        invoice = Invoice.objects.get(code=self.invoice_data['code'])
        invoice.code = new_code
        invoice.order_id = "11"
        invoice.save()
        new_invoice = Invoice.objects.get(code=new_code)
        self.assertEqual(new_invoice.code, new_code)

    def test_delete_invoice(self):
        invoice = Invoice.objects.get(code=self.invoice_data['code'])
        invoice.delete()

        data = Invoice.objects.all()
        self.assertEqual(data.count(), 0)


class InvoiceItemTestCaseSuccess(TestCase, InvoiceData):
    """ Test case for Item in voice
    """
    def setUp(self):
        invoice = self.create_invoice()
        item_data = {
            'invoice':invoice,
            'details':"Detail sample",
            'quantity':3,
            'rate':45
        }
        Item.objects.create(
            invoice = item_data['invoice'],
            details = item_data['details'],
            quantity = item_data['quantity'],
            rate = item_data['rate']
        )

    def test_add_item(self):
        item = Item.objects.get(invoice__code=self.invoice_data['code'])
        self.assertEqual(item.invoice.code, self.invoice_data['code'])

    def test_edit_item(self):
        new_detail = "New detail"
        item = Item.objects.get(invoice__code=self.invoice_data['code'])
        item.details = new_detail
        item.save()

        new_item = Item.objects.get(invoice__code=self.invoice_data['code'])
        self.assertEqual(new_item.details, new_detail)

    def test_delete_item(self):
        item = Item.objects.get(invoice__code=self.invoice_data['code'])
        item.delete()

        data = Item.objects.all()
        self.assertEqual(data.count(), 0)


class InvoiceTestCaseFail(TestCase, InvoiceDataFails):
    def setUp(self):
        self.create_invoice()

    def test_add_fail(self):
        data = Invoice.objects.all()
        import pdb;pdb.set_trace()
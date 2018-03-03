import datetime
from django.db import IntegrityError
from django.test import TestCase
from invoices.models import Invoice, Item


class InvoiceData(object):
    """ Data for invoice model
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


class ItemData(InvoiceData):
    """ Data for item model
    """
    item_data = {
        'details':"Detail sample",
        'quantity':3,
        'rate':45
    }
    def create_item(self):
        invoice = self.create_invoice()
        data = Item.objects.create(
            invoice = invoice,
            details = self.item_data['details'],
            quantity = self.item_data['quantity'],
            rate = self.item_data['rate']
        )
        return data


class InvoiceTestCaseSuccess(TestCase, InvoiceData):
    """ Test case for invoice model
    """
    def setUp(self):
        self.create_invoice()
        self.invoice = Invoice.objects.get(code=self.invoice_data['code'])

    def test_add_invoice(self):
        self.assertEqual(self.invoice.code, self.invoice_data['code'])

    def test_edit_invoice(self):
        new_code = "new_code"
        invoice = self.invoice
        invoice.code = new_code
        invoice.order_id = "11"
        invoice.save()
        new_invoice = Invoice.objects.get(code=new_code)
        self.assertEqual(new_invoice.code, new_code)

    def test_delete_invoice(self):
        invoice = self.invoice
        invoice.delete()

        data = Invoice.objects.all()
        self.assertEqual(data.count(), 0)


class InvoiceItemTestCaseSuccess(TestCase, ItemData):
    """ Test case for Item in voice
    """
    def setUp(self):
        self.create_item()
        self.item = Item.objects.get(invoice__code=self.invoice_data['code'])

    def test_add_item(self):
        self.assertEqual(self.item.invoice.code, self.invoice_data['code'])

    def test_edit_item(self):
        new_detail = "New detail"
        item = Item.objects.get(invoice__code=self.invoice_data['code'])
        item.details = new_detail
        item.save()

        new_item = Item.objects.get(invoice__code=self.invoice_data['code'])
        self.assertEqual(new_item.details, new_detail)

    def test_delete_item(self):
        item = self.item
        item.delete()

        data = Item.objects.all()
        self.assertEqual(data.count(), 0)


class InvoiceTestCaseFail(TestCase, InvoiceData):
    """ Test invoice fails
    """
    def setUp(self):
        self.invoice = self.create_invoice()

    def test_add_fail(self):

        def create_invoice_fail():
            try:
                Invoice.objects.create(
                    code = None,
                    order_id = self.invoice_data['order_id'],
                    invoice_date = self.invoice_data['invoice_date'],
                    terms = None,
                    due_date = self.invoice_data['due_date'],
                    notes = self.invoice_data['notes'],
                    conditions = self.invoice_data['conditions'],
                    date_created = self.invoice_data['date_created'],
                    date_updated = self.invoice_data['date_updated'],
                    status = self.invoice_data['status']
                )
            except IntegrityError:
                return False
            return True

        data = create_invoice_fail()
        self.assertEqual(data, False)

    def test_edit_fail(self):

        def edit_invoice_fail():
            try:
                self.invoice.code = None
                self.invoice.save()
            except IntegrityError:
                return False
            return True

        data = edit_invoice_fail()
        self.assertEqual(data, False)


class InvoiceItemTestCaseFail(TestCase, ItemData):
    """ Item test fails
    """
    def setUp(self):
        self.item = self.create_item()

    def test_add_fail(self):
        def create_item_fail():
            try:
                Item.objects.create(
                invoice = None,
                details = self.item_data['details'],
                quantity = self.item_data['quantity'],
                rate = self.item_data['rate']
            )
            except IntegrityError:
                return False
            return True

        data = create_item_fail()
        self.assertEqual(data, False)

    def test_edit_fail(self):
        def edit_item_fail():
            try:
                self.item.invoice = None
                self.item.details = None
                self.item.save() 
            except IntegrityError:
                return False
            return True

        data = edit_item_fail()
        self.assertEqual(data, False)

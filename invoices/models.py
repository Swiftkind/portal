from django.db import models


class Invoice(models.Model):
    """ Model for invoices
    """
    TERMS = (
            ('Due of Receipt', 'Due of Receipt'),
            ('Due End of Next Month', 'Due End of Next Month'),
            ('Due End of Month', 'Due End of Month')
        )

    STATUS = (
            ('Sent', 'Sent'),
            ('Draft', 'Draft')
        )

    code = models.CharField(max_length=16)
    order_id = models.CharField(max_length=16,null=True, blank=True)
    invoice_date = models.DateTimeField()
    terms = models.CharField(max_length=16,choices=TERMS)
    due_date = models.DateTimeField()
    notes = models.TextField(null=True, blank=True)
    conditions = models.CharField(max_length=28,null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=16, choices=STATUS)


class Item(models.Model):
    """ Model for items in invoice
    """

    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    details = models.CharField(max_length=255)
    quantity = models.IntegerField()
    rate = models.IntegerField()
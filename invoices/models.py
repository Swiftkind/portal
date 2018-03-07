from django.db import models
from django.utils import timezone
from decimal import Decimal


class InvoiceManager(models.Manager):
    """ Manager for invoice
    """
    def count_due_date(self):
        return self.get_queryset().filter(due_date__lt=timezone.now().date()).count()

    def drafts(self):
        return self.get_queryset().filter(status=Invoice.DRAFT)


class Invoice(models.Model):
    """ Model that contains invoice data
    """
    DUE_RECEIPT = 'due_receipt'
    DUE_END_NEXT_MONTH = 'due_end_next_month'
    DUE_END_MONTH = 'due_end_month'

    SENT = 'sent'
    DRAFT = 'draft'

    TERMS = (
            (DUE_RECEIPT, 'Due of Receipt'),
            (DUE_END_NEXT_MONTH, 'Due End of Next Month'),
            (DUE_END_MONTH, 'Due End of Month')
        )

    STATUS = (
            (SENT, 'Sent'),
            (DRAFT, 'Draft')
        )

    code = models.CharField(max_length=16)
    order_id = models.CharField(max_length=16,null=True, blank=True)
    invoice_date = models.DateTimeField()
    terms = models.CharField(max_length=16, choices=TERMS, default=DUE_RECEIPT)
    due_date = models.DateTimeField()
    notes = models.TextField(null=True, blank=True)
    conditions = models.CharField(max_length=28, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=16, choices=STATUS, default=DRAFT)

    invoice_objects = InvoiceManager()

    def __str__(self):
        return f'{self.code}'

    def is_due(self):
        return timezone.now().date() > self.due_date.date()

    def total_amount(self):
        if self.item_set.first():
            return self.item_set.first().amount()
        return 0

    def get_absolute_url(self):
        return f'/invoice/{self.id}/'


class Item(models.Model):
    """ Model for items in invoice
    """
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    details = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=0)
    rate = models.DecimalField(max_digits=15,
                               decimal_places=2,
                               default=Decimal('0.0')
                              )

    def __str__(self):
        return f'{self.invoice}'

    def amount(self):
        return self.quantity*self.rate

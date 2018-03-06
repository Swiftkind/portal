from django.shortcuts import render
from django.views.generic import TemplateView


from invoices.models import Invoice, Item


class DashboardView(TemplateView):
    """ Dashboard view for portal details
    """
    template_name = 'index.html'

    def get(self, *args, **kwargs):
        """ Display portal summary details
        """
        invoices = Invoice.objects.all()

        count_draft = 0
        count_due = 0

        for invoice in invoices:
            amount = 0
            items = Item.objects.filter(invoice=invoice)

            for item in items: # Get the total amount
                amount += item.quantity * item.rate
            invoice.amount = amount

            if invoice.status == Invoice.DRAFT: # Count draft status
                count_draft += 1

            if invoice.is_due(): # Count due dates
                count_due += 1

        context = {
            'drafts': count_draft,
            'dues': count_due,
            'no_invoice': Invoice.NO_INVOICE,
            'invoices': invoices,
        }

        return render(self.request, self.template_name, context)
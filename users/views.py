from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView


from invoices.models import Invoice


class DashboardView(LoginRequiredMixin, TemplateView):
    """ Dashboard view for portal details
    """
    template_name = 'index.html'

    def get(self, *args, **kwargs):
        """ Display portal summary details
        """
        invoices = Invoice.invoice_objects
        context = {
            'drafts': invoices.drafts().count(),
            'due_dates': invoices.count_due_date(), 
            'invoices': invoices.all(),
        }
        return render(self.request, self.template_name, context)
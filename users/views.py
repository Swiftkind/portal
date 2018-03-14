from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.utils.decorators import method_decorator
from invoices.models import Invoice
from users.forms import LoginForm
from users.decorators import user_is_logged


class DashboardView(LoginRequiredMixin, TemplateView):
    """ Dashboard view for portal details
    """
    template_name = 'dashboard.html'

    def get(self, *args, **kwargs):
        """ Display portal summary details
        """
        invoice_list = Invoice.objects.all().order_by('-date_updated')
        paginator = Paginator(invoice_list, 10)

        page = self.request.GET.get('page')
        invoices = paginator.get_page(page)
        context = {
            'drafts': Invoice.objects.drafts().count(),
            'due_dates': Invoice.objects.past_due().count(), 
            'invoices': invoices,
        }
        return render(self.request, self.template_name, context)


@method_decorator(user_is_logged, name='dispatch')
class LoginView(TemplateView):
    """ View for user login
    """
    template_name = 'users/login.html'

    def get(self, *args, **kwargs):
        form = LoginForm()
        return render(self.request, self.template_name, {'form':form})

    def post(self, *args, **kwargs):
        form = LoginForm(self.request.POST)

        if form.is_valid():
            login(self.request, form.user)
            return redirect('dashboard')

        return render(self.request, self.template_name,
                      {'form':form}, status=400)

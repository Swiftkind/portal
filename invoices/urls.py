from django.urls import path
from invoices.views import (InvoicesAPI,
                            InvoiceAPI,
                            InvoiceTermsViewset,
                            LatestInvoice)


urlpatterns = [
    path('', InvoicesAPI.as_view({'get':'list',
                                  'post':'create',
                               }), name='invoices'),
    path('<int:inv_id>/', InvoiceAPI.as_view({'get':'detail',
                                              'patch':'update',
                                           }), name='invoice'),
    path('terms/', InvoiceTermsViewset.as_view({'get':'list'}), name='api_invoice_terms'),
    path('latest/', LatestInvoice.as_view({'get':'detail'}), name='api_latest_invoice')
]
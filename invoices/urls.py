from django.urls import path
from invoices.views import (InvoicesAPI,
                            InvoiceAPI)


urlpatterns = [
    path('', InvoicesAPI.as_view({'get':'list',
                                  'post':'create',
                               }), name='invoices'),
    path('<int:inv_id>/', InvoiceAPI.as_view({'get':'detail',
                                              'patch':'update',
                                           }), name='invoice'),
    path('terms/', InvoicesAPI.as_view({'get':'terms'}), name='invoice_terms'),
    path('latest/', InvoicesAPI.as_view({'get':'latest'}), name='latest_invoice')
]
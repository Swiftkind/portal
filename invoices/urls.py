from django.urls import path
from invoices.views import (InvoicesAPI,
                            InvoiceAPI)


urlpatterns = [
    path('', InvoicesAPI.as_view({'get':'list',
                                  'post':'create',
                               }), name='invoices'),
    path('<int:inv_id>/', InvoiceAPI.as_view({'get':'detail',
                                              'patch':'update',
                                           }), name='invoice')
]
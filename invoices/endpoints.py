from django.urls import path
from invoices.api import InvoiceAPI, InvoicesAPI


urlpatterns = [
    path('invoices', InvoicesAPI.as_view(), name='api_invoices'),
    path('invoices/<int:id>/', InvoiceAPI.as_view(), name='api_invoice'),

]
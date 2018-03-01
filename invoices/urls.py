from django.urls import path
from invoices.views import InvoiceView


urlpatterns = [
    path('invoices/', InvoiceView.as_view(), name='invoice'),
]
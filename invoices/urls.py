from django.urls import path
from invoices.views import InvoiceView


urlpatterns = [
    path('invoice/', InvoiceView.as_view(), name='invoice'),
]
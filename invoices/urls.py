from django.urls import path
from invoices.views import InvoicesViewset


urlpatterns = [
    path('', InvoicesViewset.as_view({'get': 'list'}), name='api_invoices'),
]
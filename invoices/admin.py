from django.contrib import admin
from invoices.models import Invoice, Item

admin.site.register(Invoice)
admin.site.register(Item)
from django.core.paginator import EmptyPage
from rest_framework import pagination
from rest_framework.response import Response
from invoices.models import Invoice

class CustomPagination(pagination.PageNumberPagination):
    """ Custom pagination
    """
    page_size = 10

    def get_paginated_response(self, data):
        try:
            next_page_number = self.page.next_page_number()
        except EmptyPage:
            next_page_number = self.page.paginator.num_pages

        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
                'page': (self.get_next_link()[:-1] 
                         if self.get_next_link() 
                         else self.get_previous_link()[:-1]
                ),
            },
            'page': {
                'count': self.page.paginator.count,
                'has_other_pages': self.page.has_other_pages(),
                'has_previous': self.page.has_previous(),
                'page_range': list(self.page.paginator.page_range),
                'number': self.page.number,
                'has_next': self.page.has_next(),
                'next_page_number': next_page_number,
            },
            'results': data,
            'drafts': Invoice.objects.drafts().count(),
            'due_dates': Invoice.objects.past_due().count(),
        })


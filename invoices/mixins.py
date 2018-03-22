from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from invoices.models import Invoice


class Paginate(PageNumberPagination):
    """ paginate the query result
    """
    def next_page(self):
        """ Set next page
        """
        if not self.page.has_next():
            return None
        return {self.page_query_param : self.page.next_page_number()}

    def previous_page(self):
        """ Set previous page
        """
        if not self.page.has_previous():
            return None
        page_number = self.page.previous_page_number()
        if page_number == 1:
            return {self.page_query_param:1}
        return {self.page_query_param:page_number}

    def paginate(self, query):
        query = self.paginate_queryset(query, self.request)
        serializer = self.serializer_class(query, many=True)

        return {
            'page': {
                'count': self.page.paginator.count,
                'has_next': self.page.has_next(),
                'has_other_pages': self.page.has_other_pages(),
                'has_previous': self.page.has_previous(),
                'page_range': list(self.page.paginator.page_range),
                'previous': self.previous_page(),
                'next': self.next_page(),
                'number': self.page.number,
            },
            'result': serializer.data,
        }
from django.db import models


class Customer(models.Model):
    """ Models that contains the data of customer
    """
    first_name = models.CharField(max_length=40, null=True, blank=True)
    last_name = models.CharField(max_length=40, null=True, blank=True)
    company = models.CharField(max_length=40, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    billing_address = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.email}'

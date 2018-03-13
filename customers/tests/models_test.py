from django.db import IntegrityError
from django.test import TestCase
from customers.models import Customer


customer_data = {
    'first_name':'John',
    'last_name':'Doe',
    'company':'New Company',
    'email':'john@john.com',
    'billing_address':'Davao City'
}


class CustomerTestCase(TestCase):
    """ Test for customers models
    """

    def test_string_repr(self):
        """ Checks the representation string of the model
        """
        customer = Customer(**customer_data)
        self.assertEqual(str(customer), customer.email)

    def test_create_customer_success(self):
        """ Create a customer and save to database
        """
        customer = Customer.objects.create(**customer_data)

        self.assertTrue(isinstance(customer, Customer))
        self.assertEqual(customer.__str__(), customer_data['email'])

    def test_update_customer_success(self):
        """ Update a customer and save to database
        """
        customer = Customer.objects.create(**customer_data)

        self.assertTrue(isinstance(customer, Customer))

        email= 'doe2018@john.com'
        customer.email = email
        customer.save()

        self.assertEqual(customer.__str__(), email)

    def test_delete_customer_success(self):
        """ Deletes an existing customer in database
        """
        customer = Customer.objects.create(**customer_data)

        self.assertTrue(isinstance(customer, Customer))

        customer.delete()

        with self.assertRaises(Customer.DoesNotExist):
            Customer.objects.get(email=customer_data['email'])

    def test_create_customer_fails(self):
        """ Creates customer with no email
        """
        with self.assertRaises(IntegrityError):
            Customer.objects.create(
                        email=None,
                        billing_address=customer_data['billing_address']
                    )

    def test_update_customer_fails(self):
        """ Updates customer with no email
        """
        customer = Customer.objects.create(**customer_data)

        self.assertTrue(isinstance(customer, Customer))

        with self.assertRaises(IntegrityError):
            customer.email = None
            customer.save()

    def test_delete_customer_fails(self):
        """ Deletes an item that doesn't exist
        """
        customer = Customer.objects.create(**customer_data)

        self.assertTrue(isinstance(customer, Customer))

        with self.assertRaises(Customer.DoesNotExist):
            new_customer = Customer.objects.get(email='mac@jordan.com')
            new_customer.delete()

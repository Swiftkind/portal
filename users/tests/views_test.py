from django.urls import reverse
from django.utils import timezone
from django.test import TestCase, Client
from invoices.models import Invoice
from users.models import User


date_now = timezone.now().date()

invoice_data = {
    'order_id':"12",
    'invoice_date':date_now,
    'terms':Invoice.DUE_RECEIPT,
    'due_date':date_now + timezone.timedelta(days=5),
    'notes':"sample notes",
    'conditions':"condition 1",
    'date_created':date_now,
    'date_updated':date_now,
    'status':Invoice.SENT
}


user_data = {
    'email': 'john@john.com',
    'first_name': "John",
    'last_name': "Doe",
    'password': User.objects.make_random_password(),
    'image': 'assets/images/profile-default.png'
}


class DashboardTestCase(TestCase):
    """ Test dashboard
    """
    def setUp(self):
        self.client = Client()
        user = User.objects.create_user(**user_data)
        self.client.login(email=user_data['email'], password=user_data['password'])

    def test_dashboard_not_authenticated(self):
        """ Test dashboard with user not authenticated
        """
        self.client.logout()
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)

    def test_dashboard_authenticated(self):
        """ Test dashboard with user authenticated
        """
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_invoice_empty(self):
        """ Test empty invoice
        """
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.context['invoices'].count(), 0)

    def test_invoice_count(self):
        """ Test the invoice number of users
        """
        Invoice.objects.create(code='abcd', **invoice_data)
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.context['invoices'].count(), 1)


class LoginTestCase(TestCase):
    """ Test case for user login view
    """
    def setUp(self):
        self.client = Client()
        User.objects.create_user(**user_data)

    def test_get_login_page(self):
        """ Gets the login page
        """
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_post_login_page(self):
        """ Post data to login page
        """
        creds = {
            'email':user_data['email'],
            'password':user_data['password']
        }

        response = self.client.post(reverse('login'), creds)
        self.assertEqual(response.status_code, 302)

    def test_post_login_page_fail_wrong_password(self):
        """ Post data to login page with wrong password
        """
        creds = {
            'email':user_data['email'],
            'password':'1234567890'
        }

        response = self.client.post(reverse('login'), creds)
        self.assertEqual(response.context['form'].errors['__all__'].as_data()[0].code,
                         'invalid_credentials')

    def test_post_login_page_fail_no_email(self):
        """ Post data to login page with no email
        """
        creds = {
            'email':'',
            'password':user_data['password']
        }

        response = self.client.post(reverse('login'), creds)
        self.assertEqual(response.context['form'].errors['email'].as_data()[0].code,
                         'required')

    def test_post_login_page_fail_invalid_email(self):
        """ Post data to login page with invalid email
        """
        creds = {
            'email':'john@doe',
            'password':user_data['password']
        }

        response = self.client.post(reverse('login'), creds)
        self.assertEqual(response.context['form'].errors['email'].as_data()[0].code,
                         'invalid')

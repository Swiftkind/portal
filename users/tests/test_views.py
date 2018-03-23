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
        """ Setting up test
        """
        self.client = Client()
        User.objects.create_user(**user_data)


    def test_post_login_page(self):
        """ Post data to login page
        """
        creds = {
            'email':user_data['email'],
            'password':user_data['password']
        }

        response = self.client.post(reverse('login'), creds)
        self.assertIn('token', response.json())
        self.assertEqual(response.status_code, 200)


    def test_post_login_invalid_password_fails(self):
        """ Post data to login page with wrong password
        """
        creds = {
            'email':user_data['email'],
            'password':'123456'
        }

        response = self.client.post(reverse('login'), creds)
        self.assertIn('password', response.json())
        self.assertEqual('Ensure this field has at least 8 characters.', response.json().get('password')[0])
        self.assertEqual(response.status_code, 400)


    def test_login_invalid_credentials_fails(self):
        """ Post request to login page with invalid credentials.
        """
        creds = {
            'email': 'john@mail.com',
            'password': '132542351'
        }
        response = self.client.post(reverse('login'), creds)
        self.assertIn('non_field_errors', response.json())
        self.assertEqual('Invalid Email or Password.', response.json().get('non_field_errors')[0])
        self.assertEqual(response.status_code, 400)


    def test_post_login_no_email_fails(self):
        """ Post data to login page with no email
        """
        creds = {
            'email':'',
            'password':user_data['password']
        }

        response = self.client.post(reverse('login'), creds)
        self.assertIn('email', response.json())
        self.assertEqual('This field may not be blank.', response.json().get('email')[0])
        self.assertEqual(response.status_code, 400)


    def test_post_login_invalid_email_fails(self):
        """ Post data to login page with invalid email
        """
        creds = {
            'email':'john@doe',
            'password':user_data['password']
        }

        response = self.client.post(reverse('login'), creds)
        self.assertIn('email', response.json())
        self.assertEqual('Enter a valid email address.', response.json().get('email')[0])
        self.assertEqual(response.status_code, 400)

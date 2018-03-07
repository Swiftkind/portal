from django.urls import reverse
from django.test import TestCase, Client
from users.models import User


user_data = {
    'email': 'john@john.com',
    'first_name': "John",
    'last_name': "Doe",
    'password': User.objects.make_random_password()
}


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

from django.db import IntegrityError
from django.test import TestCase


from ..models import User


user_data = {
    'email': "john@doe.com",
    'first_name': "John",
    'last_name': "Doe",
    'password': User.objects.make_random_password()
}


class UserTestCase(TestCase):
    """ Testcase for user
    """
    def test_string_repr(self):
        """ Check the string representation of the model
        """
        user = User.objects.create_user(**user_data)
        self.assertEqual(user.__str__(), user.email)

    def test_create_user(self):
        """ Create user account and save
        """
        user = User.objects.create_user(**user_data)
        self.assertIsInstance(user, User)
        self.assertEqual(user.__str__(), user_data['email'])

    def test_update_user(self):
        """ Update the existing user and save
        """
        user = User.objects.create_user(**user_data)
        self.assertIsInstance(user, User)

        new_first_name = "Mark"
        user.first_name = new_first_name
        user.save()

        self.assertEqual(user.__str__(), user_data['email'])
        self.assertEqual(user.first_name, new_first_name)

    def test_delete_user(self):
        """ Delete an existing user
        """
        user = User.objects.create_user(**user_data)
        self.assertIsInstance(user, User)

        user.delete()

        with self.assertRaises(User.DoesNotExist):
            User.objects.get(email=user_data['email'])

    def test_create_user_fail(self):
        """ Create user account with invalid data
        """
        new_user_data = user_data.copy()
        new_user_data['first_name'] = None

        with self.assertRaises(IntegrityError):
            User.objects.create_user(**new_user_data)

    def test_update_user_fail(self):
        """ Update the existing user with invalid data
        """
        user = User.objects.create_user(**user_data)
        self.assertIsInstance(user, User)

        new_first_name = None
        user.first_name = new_first_name

        with self.assertRaises(IntegrityError):
            user.save()
            

    def test_delete_user_fail(self):
        """ Delete a non-existing user
        """
        with self.assertRaises(User.DoesNotExist):
            user = User.objects.get(email=user_data['email'])
            user.delete()

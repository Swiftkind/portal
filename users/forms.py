from django import forms
from django.contrib.auth import authenticate

from users.models import User


class LoginForm(forms.Form):
    """ Form for login user view
    """
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    error_msg = "Invalid Email/Password."

    def clean(self):
        """ validate user's credentials
        """
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        self.user = authenticate(email=email, password=password)

        if not self.user or not self.user.is_active:
            raise forms.ValidationError(self.error_msg,
                                        code='invalid_credentials')

        return self.cleaned_data

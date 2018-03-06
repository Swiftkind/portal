from django import forms
from django.contrib.auth import authenticate


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

        if self.user is None or not self.user.is_active:
            raise forms.ValidationError(self.error_msg, code='400')

        return self.cleaned_data

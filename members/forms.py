from django import forms

# This is the form class for our login page.
# It defines the two fields we expect from the user:
# mobile_number and password.
class LoginForm(forms.Form):
    # The mobile number field is a CharField, which is a simple text input.
    mobile_number = forms.CharField(
        label='Mobile Number',
        max_length=10,
        widget=forms.TextInput(attrs={
            'class': 'form-input w-full',  # Uses your Tailwind CSS class
            'placeholder': 'Enter your mobile number'
        })
    )
    # The password field is also a CharField, but we use a PasswordInput widget
    # to hide the text as the user types.
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-input w-full', # Uses your Tailwind CSS class
            'placeholder': 'Enter your password'
        })
    )

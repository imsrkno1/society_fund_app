from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import CustomUser, Transaction, Payment

# Form for user login
class LoginForm(forms.Form):
    mobile_number = forms.CharField(label="Mobile Number", max_length=15,
                                  widget=forms.TextInput(attrs={'class': 'form-input mt-1 w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-input mt-1 w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}))

# Form for user registration
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('mobile_number', 'name', 'house_no')

# Form for adding a new transaction
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['title', 'description', 'amount', 'transaction_type']

# Form for paying dues
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['user', 'amount_due', 'month']

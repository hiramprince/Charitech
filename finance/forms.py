from django.contrib.auth.forms import UserCreationForm
from django import forms

from finance.models import User
class UserRegistrationForm (UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length =25)
    last_name = forms .CharField(max_length = 25)

    class Meta:
        model = User
        fields =['first_name','last_name','username','email','password1','password2']
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# create your account form here 
class SignUpForm(UserCreationForm):
   
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')
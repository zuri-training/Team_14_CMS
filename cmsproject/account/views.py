from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from . import forms

# Create your views here.

# sign up view
class SignUpView(generic.CreateView):
    form_class = forms.SignUpForm
    
    # if the sign up is successful it redirects to the login page
    success_url = reverse_lazy('account:login')
    
    # directory of the used template
    template_name = 'account/signup.html'

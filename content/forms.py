from django import forms
from django.forms import ModelForm, DateInput
from django.contrib.auth.models import User
from .models import *

class EmailForm(ModelForm):
    email = forms.EmailField(label="Email", required=True)
   
    class Meta:
      model = Emails
      exclude = ['created_at','edited_at','message','subject']
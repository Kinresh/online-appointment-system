from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'
        widgets={
            'emailAddress': forms.EmailInput() ,
            'name': forms.TextInput(),
            'phno': forms.TextInput(),
        }
        labels={
            'emailAddress': 'Your Email Address',
            'name': 'Name',
            'phno': 'Phone Number',
        }
        

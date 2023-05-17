from django import forms

# Create a function 

class loginform(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=60)
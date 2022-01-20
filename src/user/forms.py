from django import forms

from user.models import User

class UserSignupForm(forms.Form):
    username = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=60, required=True)
    password = forms.CharField(max_length=150, required=True)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        user = User.objects.filter(username=username)

        if user.exists():
            raise forms.ValidationError('a user with that username already exists.')

        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = User.objects.filter(email=email)

        if user.exists():
            raise forms.ValidationError('a user with that email already exists.')

        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        c_password = self.data.get('c_password')

        if password != c_password:
            raise forms.ValidationError('passwords do not match!.')

        return password
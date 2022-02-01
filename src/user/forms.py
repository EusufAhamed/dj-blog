from django import forms
from ckeditor.widgets import CKEditorWidget

from user.models import User

class UserSigninForm(forms.Form):
    email = forms.EmailField(max_length=30, required=True)
    password = forms.CharField(max_length=150, required=True)

class UserSignupForm(forms.Form):
    username = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=60, required=True)
    password = forms.CharField(max_length=150, required=True)
    name = forms.CharField(max_length=60, required=True)

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

class UserProfileUpdateForm(forms.Form):
    name = forms.CharField(max_length=60, required=False)
    about = forms.CharField(widget=CKEditorWidget(), required=False)
    profile_image = forms.ImageField(required=False)
    cover_image = forms.ImageField(required=False)
    facebook = forms.URLField(required=False)
    twitter = forms.URLField(required=False)
    google_plus = forms.URLField(required=False)
    instagram = forms.URLField(required=False)
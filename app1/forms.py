from django import forms
from .models import Signup1,Image

class SignupForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=9,min_length=3)
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput,max_length=9,min_length=3)
    class Meta():
        model=Signup1
        fields='__all__'

class LoginForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=9,min_length=3)
    class Meta():
        model=Signup1
        fields=('Email','Password')

class ImageUploadForm(forms.ModelForm):
    class Meta():
        model=Image
        fields='__all__'

class UpdateForm(forms.ModelForm):
    class Meta():
        model=Signup1
        fields=('Name','Age','Email','Photo')

class ChangePasswordForm(forms.Form):
    OldPassword=forms.CharField(widget=forms.PasswordInput,max_length=9,min_length=3)
    NewPassword=forms.CharField(widget=forms.PasswordInput,max_length=9,min_length=3)
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput,max_length=9,min_length=3)
    
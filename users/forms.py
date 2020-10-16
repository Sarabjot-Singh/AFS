from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    field_order = ['username','email','password1','password2']

class ProfileRegistrationForm(forms.ModelForm):
    mobile = forms.IntegerField()

    class Meta:
        model = Profile
        fields = ['mobile']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'mobile']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class RechargeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['balance']

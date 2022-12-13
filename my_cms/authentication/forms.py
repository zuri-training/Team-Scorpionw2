from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.EmailInput(attrs={'class':'inputbox'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'inputbox'}))

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)


class CustomUserCreationForm(UserCreationForm):

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'fields', 'required': True, 'type':'password', 'placeholder':'Password'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'fields', 'required': True, 'type':'password', 'placeholder':'Confirm Password'}),
    )
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'phone_no')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'fields', 'required': True, 'placeholder': "First Name  (eg: John)"}),
            'last_name': forms.TextInput(attrs={'class': 'fields', 'required': True, 'placeholder': "Last Name  (eg: Doe)"}),
            'email': forms.EmailInput(attrs={'class': 'fields', 'required': True, 'placeholder': "Email  (eg: JohnDoe@gmail.com)"}),
            'phone_no': forms.TextInput(attrs={'class': 'fields', 'required': True, 'placeholder': "Phone Number"}),
        }

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'phone_no')
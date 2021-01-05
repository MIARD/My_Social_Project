from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from App_Login.models import UserProfile


class CreateNewUser(UserCreationForm):
    email = forms.EmailField(required=True, label="", widget=forms.TextInput(
        attrs={'placeholder': 'Email'}))
    username = forms.CharField(required=True, label="", widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(
        required = True,
        label="",
        widget = forms.PasswordInput(attrs={'placeholder':'Password'})
    )
    password2 = forms.CharField(
        required = True,
        label="",
        widget = forms.PasswordInput(attrs={'placeholder':'Confirm Password'})
    )

    class Meta:
        model = User
        fields = ( 'username', 'email', 'password1', 'password2')

class LoginUser(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginUser,self).__init__(*args,**kwargs)
    username = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(attrs={'placeholder':'Username'})
    )
    password = forms.CharField(
        required = True,
        label="",
        widget=forms.PasswordInput(attrs={'placeholder':"Password"})
    )

class EditProfile(forms.ModelForm):
    dob = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':'3','cols':"50"}))
    class Meta:
        model = UserProfile
        exclude = ('user',)

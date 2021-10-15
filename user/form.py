from django import forms


class UserRegistrationForm(forms.Form):
    user_id = forms.CharField()
    user_email = forms.EmailField()
    user_password = forms.CharField(widget=forms.PasswordInput())

from django.contrib.auth.models import User
from django import forms

USER_TYPES= (
    ("Developer", ("Developer")),
    ("Customer", ("Customer"))
)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=USER_TYPES, required=True)


    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'user_type']

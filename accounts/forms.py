from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    """
    You can add more fields as needed
    """
    # additional fields
    email = forms.EmailField(unique=True, required=True)

    # model to use
    class Meta:
        model = User
        fields = ("Username", "email", "password1", "password2")

    # a function to save cleaned data from the form
    def save(self, commit=True):
        user = super(RegisterForm, commit=False) # super function is refering to Parent class
        user.email = self.cleaned_data["email"] # handling additional fields
        if commit:
            user.save()
        return user

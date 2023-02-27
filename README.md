# django-auth
## Step 1: Create a directory to work and navigate into it
* Use the command: ``mkdir django && cd django ``

## Step 2: Create virtual environment and activate it 
* Use the command:``python -m venv myenv``
* To activate virtualenv windows use: ``.\myenv\Scripts\activate``
* To activate virtualenv Linux/Mac use: `` source myenv/bin/activate``

## Step 3: Install django
* Use command:   `` pip install django  `` or ``python -m pip install django ``


## Step 4: Create Django project named `` django-auth ``
* Use command: `` django-admin startproject django-auth . ``

## Step 5: Create Django app named ``accounts``
* Use command: ``python manage.py startapp accounts``

## Register your ``accounts`` app in ``settings.py`` file in ``INSTALLED_APPS`` list
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts' # new app added
]
```

## User registration
* Django comes with a built-in user registration form. We just need to configure it to our needs

### Let's start by creating user registration form
* Navigate to your app ``accounts`` folder and create a file named ``forms.py``

    ### Please Understand this
    * Django comes with a pre-built register form called ``UserCreationForm`` that connects to the pre-built model ``User``. 
    * __NOTE__: The ``UserCreationForm`` only requires a ``username`` and ``password`` (``password1`` is the initial password and ``password2`` is the password confirmation). Don't worry you will see this in work
    * We can **customize** this built-in form using ``forms.py`` that we created inside the app ``account`` folder
    * Let's call ``UserCreationForm`` within a new class called ``RegisterForm`` in ``forms.py `` and add another field called ``email``. Save the email to the user.

## make sure you have this in ``forms.py ``
```
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
```
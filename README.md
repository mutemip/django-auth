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

Run migrate command: ``python manage.py migrate``
Create super user using: ``python manage.py createsuperuser``

## Step 5: Create Django app named ``accounts``
* Use command: ``python manage.py startapp accounts``

## Step 6: Register your ``accounts`` app in ``settings.py`` file in ``INSTALLED_APPS`` list
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

## Step 7: User registration
* Django comes with a built-in user registration form. We just need to configure it to our needs

### Let's start by creating user registration form
* Navigate to your app ``accounts`` folder and create a file named ``forms.py``

    ### Please Understand this
    * Django comes with a pre-built register form called ``UserCreationForm`` that connects to the pre-built model ``User``. 
    * __NOTE__: The ``UserCreationForm`` only requires a ``username`` and ``password`` (``password1`` is the initial password and ``password2`` is the password confirmation). Don't worry you will see this in work
    * We can **customize** this built-in form using ``forms.py`` that we created inside the app ``account`` folder
    * Let's call ``UserCreationForm`` within a new class called ``RegisterForm`` in ``forms.py `` and add another field called ``email``. Save the email to the user.


## Step 8: make sure you have this in ``forms.py ``
```
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    """
    You can add more fields as needed
    """
    # additional fields
    email = forms.EmailField(required=True)

    # model to use
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    # a function to save cleaned data from the form
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False) # super function is refering to Parent class
        user.email = self.cleaned_data["email"] # handling additional fields
        if commit:
            user.save()
        return user

```
## Let's go to ``views.py`` and write a ``Register_View`` function to handle our logic

```
    from django.shortcuts import render, redirect
    from .forms import RegisterForm
    from django.contrib.auth import login
    from django.contrib import messages

    # Our register view
    def register_View(request):
        form = RegisterForm()
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save() # save passed data
                login(request, user) # login the user
                messages.success(request, "Registration Successful")
                return redirect("/")
            messages.error(request, "Invalid information")
        return render(request, "register.html", {"register_form": form})
```
__NOTE__:
* we import ``RegisterForm`` from **forms.py** file and ``login`` from ``django.contrib.auth`` and the created a ``register_view`` function

* There are two if/else statements within the function. The first checks to see if the form is being posted while the second checks to see if the form is valid. If both are True, then the form information is saved under a user, the user is logged in, and the user is redirected to the homepage showing a success message.

* Else, if the form is not valid, an error message is shown. But if the request is not a POST in the first place, meaning the first if statement returned False, render the empty form in the register template. 

* Please note that if you wish to add messages to your Django project you must enable the Messages Framework and import messages at the top of views.py. 


## Add ``urls.py`` file inside ``accounts`` app and configure our ``register_view`` in it.

```
    from django.urls import path
    from . import views

    urlpatterns = [
        path('register/', views.register_View, name="register"),
    ]

```

## Include ``apps level`` urls.py file in ``project level`` urls.py, import ``include`` function

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("accounts.urls"))
]

```



## Step : Create a folder named ``templates`` inside your app ``accounts `` folder 
* Create `` register.html `` file in the ``templates`` folder

### write this code in it, to call ``register_form`` key in ``{{}}`` tags
```
    <div class="container py-5">
        <h1>Register</h1>
        <form method="POST">
            {% csrf_token %}
            {{ register_form }}                    
            <button class="btn btn-primary" type="submit">Register</button>
        </form>
        <p class="text-center">If you already have an account, <a href="/login">login</a> instead.</p>
    </div>

```

## Let's style our Register form using ``Django-Crispy forms``
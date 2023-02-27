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

### Let's start by creating user registration
* Navigate to your app ``accounts`` folder and create a file named ``forms.py``

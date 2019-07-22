# Library

This Django Rest Framework application simulates library operation.

# How to use

To begin, set up your database in ```settings.py```. Like this:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'library',
        'USER': 'librarian',
        'PASSWORD': '12345678',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

Then you need to provide initial data for models. How to do this can be found here [Django Documentation](https://docs.djangoproject.com/en/2.2/howto/initial-data/). Or you can use your data.

# Quickstart

Python 3 should be already installed. Then use pip to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

Then run the test server:

```bash
$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
July 22, 2019 - 20:33:33
Django version 2.2.3, using settings 'library.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

# Project Goals

The code is written for educational purposes.

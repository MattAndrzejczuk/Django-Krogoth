




#### INSTALL FOR STAGING ENVIRONMENT

It's recommended that you develop your Krogoth projects using PyCharm professional.
Below are the steps you need to take before switching over to SQL light for a staging environment.
First make sure that your settings that the `settings.py` something like this:

```python3
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR + '/db.sqlite3',
    }
}
```

Once you switch to SQL light database they're going to need to run the following two commands to 
reinstall the built-in front-end Kroger off the entries as well as the core foundation.

```bash



```
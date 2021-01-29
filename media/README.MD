## THIS DIRECTORY IS FOR DEVELOPMENT ONLY

i.e. if you want to test your project locally in PyCharm and upload test files to access here:

``http://127.0.0.1:8000/media/krogoth_example_imageuploads/1610317000338.png``

Then the following needs to be overridden:

###### **_settings_staging.py_**
```python3
STATIC_URL = '/static/' # static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = ('/usr/src/volatile/static/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # user uploads root path
MEDIA_URL = '/media/'
```

###### **_urls.py_**
```python3
from jawn import settings_staging

urlpatterns = [
    path('krogoth_examples/', include('krogoth_gantry.routes.urls_krogoth_examples')),
    
# . . .
```

#### serve from project root instead of docker's `/usr/src/volatile/media/` `{ UPLOADED_FILES }`
```python3    
# . . .
    
]


    if settings_staging.DEBUG:
        urlpatterns += static(settings_staging.MEDIA_URL, document_root=settings_staging.MEDIA_ROOT)

```


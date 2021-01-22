### Krogoth Static Interfaces

Every Krogoth Project Has At Least 1 `index.html`. The default index is located in `/templates/index.html`.

The **Django View** which loads this template is in:
``PROJECT_ROOT/krogoth_gantry/views/index_and_akfoundation.py``

    def index(request):

The **Django urls.py** file which contains the default URI is in:
`PROJECT_ROOT/jawn/urls.py`

    url(r'^$', index),

### Static Interfaces Are Global


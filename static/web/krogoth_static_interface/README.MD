### Krogoth Static Interfaces - KSI
##### _Last Updated For Krogoth v1.0.15_

Public Static Interfaces are global CSS, HTML, JS and other files which can be loaded from either the
/static/ URL during production (DEBUG = False) or if you're testing out edits to your global CSS theme,
they are loaded from SQL instead of the static path like so:

###### Load From SQL:
http://HOSTNAME:8000/global_static_text/save_filesystem_to_sqldb_text/toolbar.controller.js
###### Load From static like normal:
http://HOSTNAME:8000/static/web/krogoth_static_interface/css/toolbar.controller.js

You'll probably want to test your new toolbar.controller.js by loading it from SQL, 
otherwise, any changes you make to it would require for you to run
`manage.py collectstatic` and also have your browser cache deleted to run and test your changes.
This is the essence of Django Krogoth, rapidly develop single paged web applications by testing it
immediatley after you save your changes.

### Edit Your Public Static Interfaces Locally, Or Via The Built-In IDE 
Krogoth has a built-in editor that allows you to make quick changes to HTML, JS, etc 
in `krogoth_static_interface`. If however you'd rather use your favorite editor like WebStorm or PyCharm, your
changes will need to be uploaded from the `/static/web/krogoth_static_interface/` path and be uploaded 
directly to the database. There's two ways to do this.

#### Upload All Code From krogoth_static_interface (slower)
run this GET request:
``http://localhost:8000/global_static_text/saveall_filesystem_to_sqldb_text``

#### Upload Specific Code Document From krogoth_static_interface (fast)
run this GET request:
``http://localhost:8000/global_static_text/save_filesystem_to_sqldb_text/toolbar.controller.js``

This is how the request is parsed:
``http://localhost:8000/global_static_text/save_filesystem_to_sqldb_text/{UNIQUE_ID}.{PATH}``

It will then upload the following folder to SQL:
`/static/web/krogoth_static_interface/JS/toolbar.controller.js`
`/static/web/krogoth_static_interface/{PATH}/{UNIQUE_ID}.{PATH}`


## Download SQL Code To Project folder
You may sometimes use Krogoth's web based IDE. If you are, you will sometimes want to download the JS or CSS files
from SQL back into the project folder like for example `/static/web/krogoth_static_interface/JS/toolbar.controller.js`

The Krogoth web IDE will keep track of any changes you make to SQL code to remind you to save them 
back into the filesystem for git to keep all external changes tracked. To see which code in SQL 
is in need of being downloaded and saved to the filesystem, make the following GET request:
`http://localhost:8000/global_static_text/get_uncommitted_docs`

```json
{
    "total": 1,
    "docs": [
        {
            "unique_id": "toolbar.controller.js",
            "path_to_doc": "/static/web/krogoth_static_interface/JS/toolbar.controller.JS",
            "file_kind": "JS",
            "date_modified": "2021-02-02 01:25:21.457585+00:00"
        }
    ]
}
```

In the example above, there's one JS file in krogoth_static_interface. So lets download it from SQL 
into our project directory:
`http://localhost:8000/global_static_text/save_sqldb_to_filesystem_text/toolbar.controller.js`

## All Finished

The work we did in the web IDE should now be visible by git. Do a git commit and push it, we've successfully
edited a JS file using a web browser, and have downloaded it for git to keep our changes saved.

---

# Some Other Draft Notes For KSIs

### List of Static Interface Types
- HTML
- CSS
- JS



### Example of Loading Static Interfaces 
Every Krogoth Project Has At Least 1 `index.html` file. The default index is located in `/PROJECT_ROOT/templates/index.html`.

The **Django View** which loads this template is in:
``PROJECT_ROOT/krogoth_gantry/views/index_and_akfoundation.py``

    def index(request):


The **Django urls.py** file which contains the default URI is in:
`PROJECT_ROOT/jawn/urls.py`

    url(r'^$', index),



### Static Interfaces Are Global
The default Krogoth project index.html uses a global CSS file for theming the entire AngularJS app.
It's located here:
``static/web/krogoth_static_interface/css/navigation_interface_core.css``

The index loading screen animation is all within a CSS file here:
``static/web/krogoth_static_interface/css/index_loading_styles.css``

### Load Them Into SQL For Debug Mode
``/Django-Krogoth/static/web/krogoth_static_interface``




### Krogoth Public Static Interfaces
##### _Last Updated For Krogoth v0.9.98_

Public Static Interfaces are useful when you'd like to import a custom font as a css file, and have that font available 
for all your Krogoth Gantry views. It is also a great place to keep the color scheme and other theming values 
in one place for your whole project.

---


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
``static/web/krogoth_static_interface/stylesheets/navigation_interface_core.css``

The index loading screen animation is all within a CSS file here:
``static/web/krogoth_static_interface/stylesheets/index_loading_styles.css``






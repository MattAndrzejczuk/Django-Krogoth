# Author - Matt Andrzejczuk

### aside from index.html, all HTML and JS loaded here takes
### advantage of the Django templating engine

from django.http import HttpResponse
from django.template import Context, Template



def example_view(request):
    template = Template('My name is, {{ name }}!')
    context = Context({'name': 'Gilang'})
    rendered = template.render(context)
    return HttpResponse(rendered)



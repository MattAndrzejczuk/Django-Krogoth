from django.db import models
from polymorphic.models import PolymorphicModel
# from django.contrib.postgres.fields import JSONField


# Create your models here.
class BaseCallbackEndpoint(PolymorphicModel):
    # class Meta:
    #     app_label = 'krogoth_3rdparty_api'
    full_uri = models.URLField(primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True)
    # uri_request_params = JSONField()

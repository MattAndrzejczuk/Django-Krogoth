from django.db import models
import uuid
import codecs
import datetime







class KPubStaticInterfaceCSS(models.Model):
    unique_id = models.CharField(primary_key=True, max_length=25)
    file_name = models.CharField(max_length=100, default='index_loading_styles.css')
    content = models.TextField(default='/* This CSS doc is empty */')
    is_enabled = models.BooleanField(default=True)

    pub_date = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.unique_id
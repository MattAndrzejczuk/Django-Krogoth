from django.db import models
from chat.models import JawnUser
# Create your models here.



class UncommitedSQL(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    code_syntax = models.CharField(max_length=25)
    edited_by = models.ForeignKey(JawnUser, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        pre_existing = UncommitedSQL.objects.filter(name=self.name)
        if len(pre_existing) > 0:
            pre_existing.first().delete()
        super(UncommitedSQL, self).save(*args, **kwargs)

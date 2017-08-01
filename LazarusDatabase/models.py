from django.db import models

# Create your models here.
from rest_auth.models import LazarusCommanderAccount





class TotalAnnihilationMod(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    picture = models.ImageField(upload_to = 'pic_folder/')
    owner = models.ForeignKey(LazarusCommanderAccount, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.name





# class TotalAnnihilationModAsset(models.Model):
#     parent = models.ForeignKey(TotalAnnihilationMod,
#                                on_delete=models.CASCADE)









class LazarusModProject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=250)
    developer = models.CharField(max_length=250)
    is_deleted = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)
    def __str__(self):
        return self.name




class LazarusModAsset(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    project_id = models.IntegerField()
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.name




class LazarusModDependency(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    system_path = models.CharField(max_length=100)
    asset_id = models.IntegerField()
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.name
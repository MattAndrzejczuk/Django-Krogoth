from django.db import models
from polymorphic.models import PolymorphicModel
from django.contrib.auth.models import User
from django.contrib.postgres.fields import HStoreField
from LazarusIV.models_tdf import CavedogBase, ModProject, LazarusBase
# Create your models here.
from LazarusIV.models import JawnUser

#    V  -  5

class ModProject(models.Model):
    author = models.ForeignKey(JawnUser, related_name='mod_developer', )
    is_public = models.BooleanField(default=True)
    
class ModPublication(models.Model):
    title = models.CharField(max_length=50, default='Untitled Mod Publication')
    description = models.TextField(max_length=1000)
    requirements = models.TextField(max_length=1000)
    support = models.TextField(max_length=1000)
    website_url = models.CharField(max_length=150, null=True, blank=True)
    total_minor_milestones = models.IntegerField(null=True, blank=True, default=1)
    total_major_milestones = models.IntegerField(null=True, blank=True, default=0)
    DISTRIBUTIONS = (
        ('alpha', 'Alpha'),
        ('beta', 'Beta'),
        ('rc', 'Release Candidate'),
        ('release', 'Release'),
    )
    kind = models.TextField(max_length=25, choices=DISTRIBUTIONS)
    is_private = models.BooleanField(default=True)

class ModBuild(models.Model):
    rated_by = models.ForeignKey(ModPublication, on_delete=models.CASCADE, related_name='distribution')
    v_major = models.IntegerField(default=0)
    v_minor = models.IntegerField(default=1)
    download_url = models.CharField(max_length=150)



class WargamePackage(models.Model):
    parent_proj = models.ForeignKey(ModProject, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    thumbnail_url = models.CharField(max_length=100)

class WargameFile(models.Model):
    pack = models.ForeignKey(WargamePackage, on_delete=models.CASCADE)
    path = models.CharField(max_length=100)
    unique_name = models.CharField(max_length=50)
    kind = models.CharField(max_length=50)
    thumbnail_url = models.CharField(max_length=100)

class WargameData(models.Model):
    pack = models.ForeignKey(WargamePackage, on_delete=models.CASCADE)
    source = models.ForeignKey(LazarusBase, on_delete=models.CASCADE)
    unique_name = models.CharField(max_length=50)
    kind = models.CharField(max_length=50)
    thumbnail_url = models.CharField(max_length=100)

class UserRating(PolymorphicModel):
    rated_by = models.ForeignKey(JawnUser, on_delete=models.CASCADE, related_name='vote_caster')
    total_votes = models.IntegerField(default=0)

class RatingCavedogBase(UserRating):
    cavedog_base_tdf = models.ForeignKey(CavedogBase, on_delete=models.CASCADE, related_name='cavedog_tdf')
    vote_value = models.IntegerField(default=1)

class RatingModPublication(UserRating):
    lazarus_published_mod = models.ForeignKey(ModPublication, on_delete=models.CASCADE, related_name='lazarus_mod_distribution')
    vote_value = models.IntegerField(default=1)

# RatingCavedogBase
# RatingModPublication
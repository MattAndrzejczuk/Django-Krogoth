from django.db import models

# Create your models here.





class GalleryCollection(models.Model):
    unique_name = models.CharField(max_length=255, unique=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    subheading = models.CharField(max_length=255)
    description = models.TextField()




class GalleryItem(models.Model):
    model_pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    title = models.CharField(max_length=255)
    subheading = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

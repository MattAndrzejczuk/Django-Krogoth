from django.db import models

# Create your models here.





class GalleryCollection(models.Model):
    unique_name = models.CharField(max_length=255, unique=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    subheading = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title



class GalleryItem(models.Model):
    parent_gallery = models.ForeignKey(GalleryCollection, on_delete=models.CASCADE)
    model_pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    title = models.CharField(max_length=255)
    subheading = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.title




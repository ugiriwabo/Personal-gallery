from django.db import models

# Create your models here.
  
class Category (models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    

class Location (models.Model): 
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name 

    

class Image(models.Model):
    title = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=1024)
    pub_date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)

    def save_image(self):
        self.save()